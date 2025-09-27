# Simulating-Genuine-Multipartite-nonlocality-on-Quantum-Computers

AUTHORS: Federico Hernán Holik, Camilo Andrés Granda Arango, Carlo Cuccu, Roberto Giuntini and Giuseppe Sergioli

The codes that we share in this repository are based on the theoretical deveopments contained in reference: arXiv:2405.01650v2 [quant-ph]

This code contains the functions allowing the user to simulate different non-locality inequalitites in quantum processors.

As a summary, using the functions contained inthis code, the user can:

(1) Produce different types of quantum states expressed in terms of quantum circuits, namely, GHZ states for N qubits and Quantum Random Circuits
for N qubits. Notice that, each quantum circuit corresponds to a unique quantum state.

(2) For each state generated, compute angles of maximal violation of Mermin or Svetlichny inequalities.

(3) Simulate the local spin measurements for each qubit using suitably chosen quantum circuits. Using these circuits, it is possible to 
compute the correlators appearing in the Svetlichny or Mermin inequalities.

(4) Once the circuits for the correlators are computed, one can run them on actual quantum processors, or on simulators.

The output is a test of a Svetlichny or Mermin inequality that can be run on a quantum processor and/or simulator.
