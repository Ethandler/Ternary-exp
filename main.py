from ternary_cpu import TernaryCPU
from rodrick_ai import RodrickAI
from ternary_nn import TernaryNeuralNetwork
import numpy as np
import time
import random

# Initialize CPU
cpu = TernaryCPU()
instructions = [
    ("SET", 0, 9),
    ("SET", 1, 3),
    ("ADD", 0, 3),
    ("JUMP", 0, 2),
]
cpu.load_program(instructions)
cpu.start()

# Initialize AI & Neural Network
rodrick = RodrickAI()
tnn = TernaryNeuralNetwork(3, 2)

# Training Loop: Feeds RODRICK inputs & rewards
training_inputs = ["Should I attack?", "What is love?", "Hello world?", "Pizza?"]
for _ in range(5):
    inp = random.choice(training_inputs)
    print(rodrick.think(inp))
    reward = random.choice([-3, 0, 3])
    rodrick.learn(inp, reward)

    # Train Neural Network
    data = np.array([[rodrick.qt.measure(), rodrick.qt.measure(), rodrick.qt.measure()]])
    expected = np.array([[9, 3]])
    tnn.train(data, expected)

    time.sleep(1)

# CLI Loop (User Input)
print("\n--- Interactive CLI with RODRICK (type 'exit' to quit) ---")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break

    print("RODRICK:", rodrick.think(user_input))
    print("Memory recall:", rodrick.recall(user_input))
    print("Emotion:", rodrick.emotional_response(user_input))

    # Training correction
    feedback = input("Type 'correct' or 'wrong' to train, or press enter to skip: ")
    if feedback.lower() in ["correct", "wrong"]:
        print(rodrick.user_feedback(user_input, feedback))

    # Neural Network Prediction
    tnn_input = np.array([[rodrick.qt.measure(), rodrick.qt.measure(), rodrick.qt.measure()]])
    print("Neural Net Guess:", tnn.forward(tnn_input))
    print("-----")

cpu.stop()
print("Final CPU State:", cpu)
print("Done. RODRICK shutting down...")
