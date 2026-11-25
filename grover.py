"""Grover-Suche mit Qiskit: findet einen markierten Zustand unter 2^n Möglichkeiten."""
import math
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

N_QUBITS = 3
TARGET = "101"          # markierter Zustand
SHOTS = 4096

def oracle(n, target):
    qc = QuantumCircuit(n)
    # Qiskit-Bitreihenfolge: Qubit 0 ist das niedrigste Bit -> String umdrehen
    for i, bit in enumerate(reversed(target)):
        if bit == "0":
            qc.x(i)
    qc.h(n - 1); qc.mcx(list(range(n - 1)), n - 1); qc.h(n - 1)
    for i, bit in enumerate(reversed(target)):
        if bit == "0":
            qc.x(i)
    return qc

def diffuser(n):
    qc = QuantumCircuit(n)
    qc.h(range(n)); qc.x(range(n))
    qc.h(n - 1); qc.mcx(list(range(n - 1)), n - 1); qc.h(n - 1)
    qc.x(range(n)); qc.h(range(n))
    return qc

def grover(n, target, iterations):
    qc = QuantumCircuit(n, n)
    qc.h(range(n))
    for _ in range(iterations):
        qc.compose(oracle(n, target), inplace=True)
        qc.compose(diffuser(n), inplace=True)
    qc.measure(range(n), range(n))
    return qc

if __name__ == "__main__":
    sim = AerSimulator()
    optimal = round(math.pi / 4 * math.sqrt(2 ** N_QUBITS))
    print(f"{N_QUBITS} Qubits, Zielzustand |{TARGET}>, optimale Iterationen: {optimal}")
    print(f"Zufälliges Raten: {1 / 2 ** N_QUBITS:.1%} Trefferwahrscheinlichkeit")
    for k in range(0, 4):
        qc = transpile(grover(N_QUBITS, TARGET, k), sim)
        counts = sim.run(qc, shots=SHOTS).result().get_counts()
        p = counts.get(TARGET, 0) / SHOTS
        print(f"Iterationen: {k}  ->  P(|{TARGET}>) = {p:.1%}")
