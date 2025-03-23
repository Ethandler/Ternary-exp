import threading
import json
import os
import time
import random
from quantum_ternary import QuantumTernary

class RodrickAI:
    """ Multi-threaded ternary AI with memory & emotions. """

    MEMORY_FILE = "rodrick_memory.json"

    EMOTIONS = {3: "Frustrated 🤬", 6: "Neutral 😐", 9: "Happy 😊"}

    def __init__(self):
        self.memory = self.load_memory()
        self.qt = QuantumTernary()
        self.learning_thread = threading.Thread(target=self.background_learning, daemon=True)
        self.learning_thread.start()

    def think(self, input_data):
        """ Processes input and stores decision dynamically. """
        dream = self.qt.measure()
        if input_data in self.memory:
            change = random.choice([-3, 0, 3])
            self.memory[input_data] = max(3, min(9, self.memory[input_data] + change))
        else:
            self.memory[input_data] = dream  # First-time response
        self.save_memory()
        return f"Processing '{input_data}' → Dream State {self.memory[input_data]}"

    def recall(self, input_data):
        """ Retrieves past memories. """
        return self.memory.get(input_data, "No memory yet")

    def learn(self, input_data, reward):
        """ Adjusts memory based on weighted learning. """
        if input_data in self.memory:
            self.memory[input_data] = max(3, min(9, self.memory[input_data] + reward))
        else:
            self.memory[input_data] = reward  # If new, set directly
        self.save_memory()

    def user_feedback(self, input_data, feedback):
        """ Allows user to correct RODRICK in real-time without flipping emotions incorrectly. """
        if input_data in self.memory:
            before = self.memory[input_data]  # Store old state

            if feedback.lower() == "correct":
                # Reinforce emotion (but cap at min/max limits)
                if before == 3:  # If already negative, keep it negative
                    self.learn(input_data, -3)
                elif before == 6:  # If neutral, move toward positive
                    self.learn(input_data, 3)
                elif before == 9:  # If already positive, keep it positive
                    self.learn(input_data, 3)
            elif feedback.lower() == "wrong":
                # Make emotion less extreme (closer to neutral)
                if before == 3:
                    self.learn(input_data, 3)  # Make less negative (closer to neutral)
                elif before == 6:
                    self.learn(input_data, -3)  # If neutral, move toward negative
                elif before == 9:
                    self.learn(input_data, -3)  # Make less positive (closer to neutral)

            after = self.memory[input_data]  # Check new state
            return f"Feedback applied: {feedback}. Memory changed from {before} → {after}"

        return "No previous memory of this input. RODRICK learned it for the first time!"




    def emotional_response(self, input_data):
        """ Determines emotional reaction to input based on memory state. """
        state = self.memory.get(input_data, 6)
        return f"RODRICK feels {self.EMOTIONS[state]} about '{input_data}'"

    def background_learning(self):
        """ Adjusts memories slightly over time. """
        while True:
            if self.memory:
                key = random.choice(list(self.memory.keys()))
                change = random.choice([-3, 0, 3])  # Small drift
                self.memory[key] = max(3, min(9, self.memory[key] + change))
                self.save_memory()
            time.sleep(2)  # Background learning interval

    def save_memory(self):
        """ Saves memory to JSON file. """
        with open(self.MEMORY_FILE, "w") as f:
            json.dump(self.memory, f)

    def load_memory(self):
        """ Loads memory from file or starts fresh. """
        if os.path.exists(self.MEMORY_FILE):
            try:
                with open(self.MEMORY_FILE, "r") as f:
                    return json.load(f)
            except json.JSONDecodeError:
                print("Corrupted memory file, starting fresh.")
                return {}
        return {}
