# %%
from qiskit_ibm_runtime import QiskitRuntimeService, RuntimeJob
from qiskit.visualization import plot_histogram
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, execute
# %%

QiskitRuntimeService.save_account(channel="ibm_quantum", token="", set_as_default=True)

# %%
num_qubits = 6
service = QiskitRuntimeService()
qr = QuantumRegister(num_qubits)
cr = ClassicalRegister(num_qubits)
circuit = QuantumCircuit(qr, cr)
# %%
simulator = service.get_backend("ibm_kyoto")
print("Guess the Number Game")
print("------------------")
print("You have 5 attempts to guess it. Press 1 to continue.")

attempts = 0
max_attempts = 5

win = False
iuser = input("Press 1 to continue.")
if iuser == "1":
    print("Generating password...")
    password = generate_password()
    print("Password generated!")
    
    while (attempts < max_attempts):
        print("Attempt", attempts+1)
        guess = int(input("Enter your guess: "))
        print("Your guess is:", guess)
        if guess == password:
            print("Congratulations! You guessed the password!")
            win = True
            break
        else:
            if guess > password:
                print("The password is smaller than your guess.")
            else:
                print("The password is greater than your guess.")
            attempts += 1
    
    if not win and input("Do you want to see the password? (y/n) ") == "y":
        print("The password is:", password)

# %%
def generate_password():
    for i in range(num_qubits):
        circuit.h(i)
        circuit.measure(qr[i], cr[i])
    
    result = execute(circuit, backend=simulator).result()

    bitstring = next(iter(result.get_counts(circuit)))
    password = int(bitstring, 2)
    print("Password:", password)
    return password
# %%
generate_password()
# %%
