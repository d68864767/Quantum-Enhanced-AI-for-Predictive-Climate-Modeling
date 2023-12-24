```python
# Import necessary modules
from qiskit import QuantumCircuit, transpile, assemble, Aer, execute
from qiskit.visualization import plot_histogram, plot_bloch_multivector

class QuantumComputing:
    def __init__(self):
        self.circuit = None

    def create_circuit(self, qubits, bits):
        # Create a Quantum Circuit acting on a quantum register of three qubits
        self.circuit = QuantumCircuit(qubits, bits)

    def add_gate(self, gate, qubit):
        # Add a gate to the circuit
        if gate.lower() == 'h':
            self.circuit.h(qubit)
        elif gate.lower() == 'x':
            self.circuit.x(qubit)
        # Add more gates as needed

    def measure(self, qubit, bit):
        # Add a measurement gate
        self.circuit.measure(qubit, bit)

    def run_simulation(self):
        # Use Aer's qasm_simulator
        simulator = Aer.get_backend('qasm_simulator')

        # Map the quantum measurement to the classical bits
        transpiled_circuit = transpile(self.circuit, simulator)

        # Run the circuit on the qasm simulator
        job = simulator.run(assemble(transpiled_circuit, simulator))

        # Grab results from the job
        result = job.result()

        # Returns counts
        counts = result.get_counts(self.circuit)
        return counts

    def integrate(self):
        # Define the number of qubits and classical bits for the circuit
        qubits = 3
        bits = 3

        # Create the quantum circuit
        self.create_circuit(qubits, bits)

        # Add gates to the circuit
        self.add_gate('h', 0)
        self.add_gate('x', 1)
        self.add_gate('h', 2)

        # Measure the qubits
        for i in range(qubits):
            self.measure(i, i)

        # Run the quantum simulation
        counts = self.run_simulation()

        # Print the results
        print(f"Results of the quantum simulation: {counts}")
```
