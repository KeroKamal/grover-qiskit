# Grover-Suche mit Qiskit

Implementierung des Grover-Algorithmus für 3 Qubits (gesuchter Zustand |101>), simuliert mit Qiskit Aer.

## Ausführen
    pip install qiskit qiskit-aer
    python grover.py

## Ergebnis (4096 Shots, Simulator)
| Iterationen | P(|101>) |
|---|---|
| 0 (Raten) | 12,3 % |
| 1 | 78,2 % |
| 2 (optimal) | 95,0 % |
| 3 | 32,9 % |

Nach der optimalen Anzahl von Iterationen (≈ π/4 · √8 = 2) steigt die Trefferwahrscheinlichkeit von 12,5 % auf 95 %.
Mit einer dritten Iteration sinkt sie wieder, weil der Zustand "überrotiert" wird.
