import os
import sys
sys.path.append("/home/artix41/Toronto/qiskit-terra/")
import qiskit
print(qiskit.__file__)
import matplotlib.pyplot as plt
import numpy as np
from qiskit.tools.visualization._circuit_visualization import circuit_drawer
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from qiskit import Aer, execute, compile

from FockWit import QMode

class CVCircuit:
    def __init__(self, circuit, qr, n_qubits_per_mode=2):
        self.n_qubits_per_mode = n_qubits_per_mode
        self.circuit = circuit
        self.qr = qr
        self.gates = CVGates(n_qubits_per_mode)

    def DGate(self, alpha, qumode):
        qmr = (qr[qumode])
        circuit.unitary(gates.D(alpha), *(qr[i] for i in range(qumode, qumode+self.n_qubits_per_mode)))


def DGate(circuit, qr, cv, qumode, alpha):
    # U = np.identity(4)
    U = cv.S(alpha)
    # print(U@U.T.conj())
    circuit.unitary(U, qr[qumode], qr[qumode+1], qr[qumode+2])

if __name__ == '__main__':
    # ===== Constants =====

    n_qubits_per_mode = 3
    n_qumodes = 1
    alpha = 0.3

    # ==== Initialize circuit =====

    qr = QuantumRegister(n_qubits_per_mode*n_qumodes)
    cr = ClassicalRegister(n_qubits_per_mode*n_qumodes)
    circuit = QuantumCircuit(qr, cr)
    cv_circuit = CVCircuit(circuit, qr, n_qubits_per_mode)

    # ==== Build circuit ====

    cv_circuit.DGate(alpha, 0)
    # circuit.measure(qr, cr)
    print(circuit)

    # ==== Compilation =====

    backend = Aer.get_backend('statevector_simulator')
    job = execute(circuit, backend)
    result = job.result()
    state = job.result().get_statevector(circuit)

    # ==== Tests ====

    print(state)

    prob = np.abs(state)**2
    plt.plot(prob,'-o')
    plt.show()