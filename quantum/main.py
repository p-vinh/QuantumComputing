from qiskit_ibm_runtime import QiskitRuntimeService
import os
from os.path import join, dirname
import dotenv

dotenv.load_dotenv("quantum\tokens.env")

# Save an IBM Quantum account and set it as your default account.
# QiskitRuntimeService.save_account(channel="ibm_quantum", token=os.environ.get("TOKEN"), set_as_default=True)
 
# # Load saved credentials
# service = QiskitRuntimeService()