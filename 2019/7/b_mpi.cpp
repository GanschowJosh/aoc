#include <mpi.h>
#include <bits/stdc++.h>

using namespace std;

const int SIGNAL = 1;

long long param(const vector<long long>& code, int curr, int offset) {
  int divisor = offset == 1 ? 100 : 1000;
  int mode = code[curr] / divisor % 10;
  long long value = code[curr + offset];
  return mode == 0 ? code[value] : value;
}

long long run(vector<long long> code, int phase, int rank) {
  int prev = (rank + 4) % 5;
  int next = (rank + 1) % 5;
  int curr = 0;
  long long last_output = 0;
  deque<long long> inps = {phase};

  if (rank == 0) inps.push_back(0);

  while (true) {
    int op = code[curr] % 100;

    if (op == 1) {
      code[code[curr + 3]] = param(code, curr, 1) + param(code, curr, 2);
      curr += 4;
    } else if (op == 2) {
      code[code[curr + 3]] = param(code, curr, 1) * param(code, curr, 2);
      curr += 4;
    } else if (op == 3) {
      long long input;
      if (!inps.empty()) {
        input = inps.front();
        inps.pop_front();
      } else {
        MPI_Recv(&input, 1, MPI_LONG_LONG, prev, SIGNAL, MPI_COMM_WORLD,
                 MPI_STATUS_IGNORE);
      }
      code[code[curr + 1]] = input;
      curr += 2;
    } else if (op == 4) {
      last_output = param(code, curr, 1);
      MPI_Ssend(&last_output, 1, MPI_LONG_LONG, next, SIGNAL, MPI_COMM_WORLD);
      curr += 2;
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
      return last_output;
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

int main(int argc, char** argv) {
  MPI_Init(&argc, &argv);

  int rank, size;
  MPI_Comm_rank(MPI_COMM_WORLD, &rank);
  MPI_Comm_size(MPI_COMM_WORLD, &size);

  if (size != 5 || argc != 2) {
    if (rank == 0) cerr << "usage: mpirun -np 5 ./b_mpi INPUT_FILE\n";
    MPI_Finalize();
    return 1;
  }

  try {
    vector<long long> original = read_program(argv[1]);
    array<int, 5> phases = {5, 6, 7, 8, 9};
    long long best = 0;

    do {
      long long last_output = run(original, phases[rank], rank);
      if (rank == 0) {
        MPI_Recv(&last_output, 1, MPI_LONG_LONG, 4, SIGNAL, MPI_COMM_WORLD,
                 MPI_STATUS_IGNORE);
      }
      if (rank == 4) best = max(best, last_output);

      MPI_Barrier(MPI_COMM_WORLD);
    } while (next_permutation(phases.begin(), phases.end()));

    if (rank == 4) cout << best << '\n';
  } catch (const exception& error) {
    cerr << "rank " << rank << ": " << error.what() << '\n';
    MPI_Abort(MPI_COMM_WORLD, 1);
  }

  MPI_Finalize();
  return 0;
}
