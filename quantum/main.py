# %%
from qiskit_ibm_runtime import QiskitRuntimeService, Sampler
from qiskit import QuantumCircuit
import os
from os.path import join, dirname
from dotenv import load_dotenv



circuit = QuantumCircuit(2, 2)

circuit.x(0)
circuit.h(0)
circuit.barrier()

circuit.measure(range(2), range(2))
circuit.draw(output='mpl', style="iqp")

