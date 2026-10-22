#include <mpi.h>
#include <bits/stdc++.h>

using namespace std;

enum Tags { RESET = 1, STEP = 2, REPLY = 3, STOP = 4 };
enum Events { NEED_INPUT = 1, OUTPUT = 2, HALT = 3 };

long long param(const vector<long long>& code, int curr, int offset) {
  int divisor = offset == 1 ? 100 : 1000;
  int mode = code[curr] / divisor % 10;
  long long value = code[curr + offset];
  return mode == 0 ? code[value] : value;
}

array<long long, 2> run(vector<long long>& code, int& curr,
                        deque<long long>& inps) {
  while (true) {
    int op = code[curr] % 100;

    if (op == 1) {
      code[code[curr + 3]] = param(code, curr, 1) + param(code, curr, 2);
      curr += 4;
    } else if (op == 2) {
      code[code[curr + 3]] = param(code, curr, 1) * param(code, curr, 2);
      curr += 4;
    } else if (op == 3) {
      if (inps.empty()) return {NEED_INPUT, 0};
      code[code[curr + 1]] = inps.front();
      inps.pop_front();
      curr += 2;
    } else if (op == 4) {
      long long out = param(code, curr, 1);
      curr += 2;
      return {OUTPUT, out};
    } else if (op == 5) {
      curr = param(code, curr, 1) ? param(code, curr, 2) : curr + 3;
    } else if (op == 6) {
      curr = !param(code, curr, 1) ? param(code, curr, 2) : curr + 3;
    } else if (op == 7) {
      code[code[curr + 3]] = param(code, curr, 1) < param(code, curr, 2);
      curr += 4;
    } else if (op == 8) {
      code[code[curr + 3]] = param(code, curr, 1) == param(code, curr, 2);
      curr += 4;
    } else if (op == 99) {
      return {HALT, 0};
    } else {
      throw runtime_error("unknown opcode " + to_string(op));
    }
  }
}

vector<long long> read_program(const string& filename) {
  ifstream file(filename);
  if (!file) throw runtime_error("could not open " + filename);

  string line, token;
  getline(file, line);
  stringstream ss(line);
  vector<long long> code;
  while (getline(ss, token, ',')) code.push_back(stoll(token));
  return code;
}

void worker(const vector<long long>& original) {
  vector<long long> code;
  deque<long long> inps;
  int curr = 0;

  while (1) {
    MPI_Status status;
    MPI_Probe(0, MPI_ANY_TAG, MPI_COMM_WORLD, &status);

    if (status.MPI_TAG == STOP) {
      MPI_Recv(nullptr, 0, MPI_BYTE, 0, STOP, MPI_COMM_WORLD,
               MPI_STATUS_IGNORE);
      return;
    }

    if (status.MPI_TAG == RESET) {
      long long phase;
      MPI_Recv(&phase, 1, MPI_LONG_LONG, 0, RESET, MPI_COMM_WORLD,
               MPI_STATUS_IGNORE);
      code = original;
      curr = 0;
      inps = {phase};
    } else {
      long long message[2];
      MPI_Recv(message, 2, MPI_LONG_LONG, 0, STEP, MPI_COMM_WORLD,
               MPI_STATUS_IGNORE);
      if (message[0]) inps.push_back(message[1]);

      auto result = run(code, curr, inps);
      MPI_Send(result.data(), 2, MPI_LONG_LONG, 0, REPLY, MPI_COMM_WORLD);
    }
  }
}

long long try_phases(const array<int, 5>& phases) {
  for (int i = 0; i < 5; ++i) {
    long long phase = phases[i];
    MPI_Send(&phase, 1, MPI_LONG_LONG, i + 1, RESET, MPI_COMM_WORLD);
  }

  array<deque<long long>, 5> inps;
  array<bool, 5> done{};
  inps[0].push_back(0);

  long long last_e_output = 0;
  int i = 0;
  while (!all_of(done.begin(), done.end(), [](bool x) { return x; })) {
    if (!done[i]) {
      long long message[2] = {0, 0};
      if (!inps[i].empty()) {
        message[0] = 1;
        message[1] = inps[i].front();
        inps[i].pop_front();
      }

      MPI_Send(message, 2, MPI_LONG_LONG, i + 1, STEP, MPI_COMM_WORLD);

      long long result[2];
      MPI_Recv(result, 2, MPI_LONG_LONG, i + 1, REPLY, MPI_COMM_WORLD,
               MPI_STATUS_IGNORE);

      if (result[0] == OUTPUT) {
        inps[(i + 1) % 5].push_back(result[1]);
        if (i == 4) last_e_output = result[1];
      } else if (result[0] == HALT) {
        done[i] = true;
      }
    }
    i = (i + 1) % 5;
  }

  return last_e_output;
}

int main(int argc, char** argv) {
  MPI_Init(&argc, &argv);

  int rank, size;
  MPI_Comm_rank(MPI_COMM_WORLD, &rank);
  MPI_Comm_size(MPI_COMM_WORLD, &size);

  if (size != 6 || argc != 2) {
    if (rank == 0) cerr << "usage: mpirun -np 6 ./b_mpi INPUT_FILE\n";
    MPI_Finalize();
    return 1;
  }

  try {
    vector<long long> original = read_program(argv[1]);

    if (rank != 0) {
      worker(original);
    } else {
      array<int, 5> phases = {5, 6, 7, 8, 9};
      long long best = 0;
      do {
        best = max(best, try_phases(phases));
      } while (next_permutation(phases.begin(), phases.end()));
      cout << best << '\n';

      for (int i = 1; i <= 5; ++i) {
        MPI_Send(nullptr, 0, MPI_BYTE, i, STOP, MPI_COMM_WORLD);
      }
    }
  } catch (const exception& error) {
    cerr << "rank " << rank << ": " << error.what() << '\n';
    MPI_Abort(MPI_COMM_WORLD, 1);
  }

  MPI_Finalize();
  return 0;
}
