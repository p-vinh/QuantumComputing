# %%
from qiskit_ibm_runtime import QiskitRuntimeService, RuntimeJob
from qiskit.visualization import plot_histogram
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, execute
# %%
QiskitRuntimeService.save_account(channel="ibm_quantum", token="586969ff64ddf7153b493eb33b685f080c73de8d387bafe20388450e9cfa6f851a6d835b4db376bff7f619db8d85acbeac283bc79591e504ee9d1d13ee9cb112", set_as_default=True)
# %%
num_qubits = 1
service = QiskitRuntimeService()
qr = QuantumRegister(num_qubits)
cr = ClassicalRegister(num_qubits)
circuit = QuantumCircuit(qr, cr)
# %%
print("Guess the Password")
print("------------------")
print("The password has 8 digits, each either 0-9.")
print("You have 3 attempts to guess it.")
print("Bolded digits indicate correct guesses in the right position.")

attempts = 0
max_attempts = 3

win = False
iuser = input("Press 1 to continue.")
if iuser == "1":
    print("Generating password...")
    password = generate_password()
    print("Password generated!")
    
    while (attempts < max_attempts):
        print("Attempt", attempts+1)
        guess = input("Enter your guess: ")
        if guess == password:
            print("Congratulations! You guessed the password!")
            win = True
            break
        else:
            print("Incorrect. Here are the bolded digits:")
            for i in range(len(password)):
                if guess[i] == password[i]:
                    print(password[i], end="")
                else:
                    print(guess[i], end="")
            print()
            attempts += 1

    if input("Do you want to see the password? (y/n) ") == "y" and not win:
        print("The password is:", password)

# %%
def generate_password():
    simulator = service.get_backend("ibmq_qasm_simulator")

    # for i in range(num_qubits):
    #     circuit.h(i)
    #     circuit.measure(qr[i], cr[i])
    #     if i < num_qubits-1:
    #         circuit.cx(i, i+1)
    circuit.h(0)
    password = ""    
    circuit.measure(qr[0], cr[0])
    
    results = execute(circuit, backend=simulator).result()
    print(results)
    for i in range(8):
        print(next(iter(results)))
    
    # bitstring = next(iter(result.get_counts(circuit)))
    # password = int(bitstring, 2)

    print(password)
# %%
generate_password()
# %%
