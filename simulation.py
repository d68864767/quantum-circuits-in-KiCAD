```python
# Import necessary libraries
from qiskit import QuantumCircuit, transpile, assemble, Aer, execute
from qiskit.visualization import plot_bloch_multivector, plot_histogram

# Define the quantum circuit
def create_quantum_circuit():
    # Create a Quantum Circuit with 2 qubits (change as per your design)
    qc = QuantumCircuit(2)

    # Add gates to your circuit (change as per your design)
    # Here, we add a Hadamard gate on qubit 0, and a CNOT gate on qubit 0 (control) and qubit 1 (target)
    qc.h(0)
    qc.cx(0, 1)

    return qc

# Simulate the quantum circuit
def simulate_quantum_circuit(qc):
    # Use Aer's qasm_simulator
    simulator = Aer.get_backend('qasm_simulator')

    # Transpile the circuit for the simulator
    transpiled_qc = transpile(qc, simulator)

    # Assemble the circuit and run the simulation
    job = simulator.run(transpiled_qc, shots=1000)

    # Grab the results from the job
    result = job.result()

    # Get the counts (how many times each result was obtained)
    counts = result.get_counts()

    return counts

# Main function
def main():
    # Create the quantum circuit
    qc = create_quantum_circuit()

    # Simulate the quantum circuit
    counts = simulate_quantum_circuit(qc)

    # Print the result counts
    print(counts)

    # Plot the result counts
    plot_histogram(counts).show()

if __name__ == "__main__":
    main()
```
