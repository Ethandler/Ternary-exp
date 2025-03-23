from ternary_cpu import TernaryCPU
from rodrick_ai import RodrickAI
from ternary_nn import TernaryNeuralNetwork
import numpy as np

print("Initializing RODRICK's Ternary CPU...")
cpu = TernaryCPU()
print("CPU initialized.")

print("Initializing RODRICK's AI system...")
rodrick = RodrickAI()
print("AI initialized.")

# Load and execute a program
program = [
    ("SET", 0, 9),   # Set Register 0 to 9 (1)
    ("SET", 1, 3),   # Set Register 1 to 3 (-1)
    ("IF-GOTO", 0, 4),  # If Register 0 is 9, jump to instruction 4
    ("SET", 2, 3),   # This line will be **skipped** if the condition is true
    ("SET", 2, 9),   # If it jumps, Register 2 gets set to 9
]

print("Loading program into CPU...")
cpu.load_program(program)
print("Executing program...")
cpu.execute()
print("Program execution complete.")

# AI Thinking and Learning
print("RODRICK is thinking...")
print(rodrick.think("What is reality?"))
print(rodrick.think("Who am I?"))

# AI recalls previous thoughts and adjusts behavior
print("AI Dream Recall:", rodrick.recall("What is reality?"))
rodrick.learn("What is reality?", 3)  # AI learns a new perspective
print("AI Dream Recall After Learning:", rodrick.recall("What is reality?"))

# Check Emotional Response
print("RODRICK's Mood:", rodrick.emotional_response("What is reality?"))

# Ternary Neural Network Test
tnn = TernaryNeuralNetwork(3, 2)
inputs = np.array([[9, 3, 6]])  # Example input
print("Neural Prediction:", tnn.forward(inputs))

# Show CPU state
print("Final CPU State:", cpu)
