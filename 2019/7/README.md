# AOC 2019 Day 7 Part 2 MPI

## problem overview

Five virtual machines (called amplifiers) execute the same Intcode program. They're connected in a feedback loop, with each amp's output serving as the next one's input. 

Each amp receives a unique initial phase setting from {5,6,7,8,9}. The system begins with an input signal of 0 and continues exchanging signals until the programs halt. 

The goal is to find the permutation of phase settings that maximize the final output of the last amplifier.

## MPI implementation

I wrote a version in MPI that simulates this exact process with each rank being one of the amps. Each rank executes its own Intcode VM, using `MPI_Ssend` and `MPI_Recv` to pass signals around the ring.

The application of MPI here is interesting because it doesn't really provide a performance advantage compared to the sequential version. The problem's structure just naturally maps onto MPI's model.

## running

- `mpic++ b_mpi.cpp -o b_mpi`
- `mpirun -np 5 ./b_mpi input`