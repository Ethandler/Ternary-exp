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
        dream = self.qt.measure()
        if input_data in self.memory:
            self.memory[input_data] = max(3, min(9, self.memory[input_data] + random.choice([-3, 0, 3])))
        else:
            self.memory[input_data] = dream
        self.save_memory()
        return f"Processing '{input_data}' => Dream State {self.memory[input_data]}"

    def recall(self, input_data):
        return self.memory.get(input_data, "No memory yet")

    def learn(self, input_data, reward):
        if input_data in self.memory:
            self.memory[input_data] = max(3, min(9, self.memory[input_data] + reward))
            self.save_memory()

    def emotional_response(self, input_data):
        state = self.memory.get(input_data, 6)
        return f"RODRICK feels {self.EMOTIONS[state]} about '{input_data}'"

    def background_learning(self):
        while True:
            if self.memory:
                key = random.choice(list(self.memory.keys()))
                self.memory[key] = max(3, min(9, self.memory[key] + random.choice([-3, 0, 3])))
                self.save_memory()
            time.sleep(2)

    def save_memory(self):
        with open(self.MEMORY_FILE, "w") as f:
            json.dump(self.memory, f)

    def load_memory(self):
        if os.path.exists(self.MEMORY_FILE):
            try:
                with open(self.MEMORY_FILE, "r") as f:
                    return json.load(f)
            except json.JSONDecodeError:
                print("Corrupted memory file, starting fresh.")
                return {}
        return {}
