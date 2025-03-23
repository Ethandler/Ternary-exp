import random
import json
import os
import threading
import time
from quantum_ternary import QuantumTernary

class RodrickAI:
    """ RODRICK: A multi-threaded, evolving ternary AI with emotional intelligence and memory persistence. """

    MEMORY_FILE = "rodrick_memory.json"  # Persistent storage file

    EMOTIONS = {
        3: "Frustrated 🤬",
        6: "Neutral 😐",
        9: "Happy 😊"
    }

    def __init__(self):
        """ Initialize AI with memory storage, emotional intelligence, and multi-threaded learning. """
        self.memory = self.load_memory()
        self.qutrit = QuantumTernary()
        self.learning_thread = threading.Thread(target=self.background_learning, daemon=True)
        self.learning_thread.start()  # Start background learning

    def think(self, input_data):
        """ AI processes input and stores decision + outcome dynamically. """
        dream_state = self.qutrit.measure()

        if input_data in self.memory:
            self.memory[input_data] = max(3, min(9, self.memory[input_data] + random.choice([-3, 0, 3])))
        else:
            self.memory[input_data] = dream_state

        self.save_memory()
        return f"Processing '{input_data}' → Dream State {self.memory[input_data]}"

    def recall(self, input_data):
        """ Recalls past decisions and adapts based on experience. """
        return self.memory.get(input_data, "No memory of this yet.")

    def learn(self, input_data, reward):
        """ Reinforcement Learning: Adjusts AI response over time based on reward. """
        if input_data in self.memory:
            self.memory[input_data] = max(3, min(9, self.memory[input_data] + reward))
            self.save_memory()

    def background_learning(self):
        """ Runs in a separate thread, continuously refining knowledge over time. """
        while True:
            if self.memory:
                random_key = random.choice(list(self.memory.keys()))
                self.memory[random_key] = max(
                    3, 
                    min(9, self.memory[random_key] + random.choice([-3, 0, 3]))
                )
                self.save_memory()
            time.sleep(5)  # Background learning every 5 seconds

    def emotional_response(self, input_data):
        """ Determines RODRICK's mood based on memory. """
        state = self.memory.get(input_data, 6)  # Default to neutral (6)
        return f"RODRICK feels {self.EMOTIONS[state]} about '{input_data}'"

    def save_memory(self):
        """ Saves AI memory to a file for persistence beyond execution. """
        with open(self.MEMORY_FILE, 'w') as file:
            json.dump(self.memory, file)

    def load_memory(self):
     """ Loads AI memory from a file to retain knowledge between executions. """
     if os.path.exists(self.MEMORY_FILE):
        try:
            with open(self.MEMORY_FILE, 'r') as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Warning: rodrick_memory.json was corrupted. Creating a new memory file.")
            return {}
     return {}


# Quick Test if you run rodrick_ai.py directly
if __name__ == "__main__":
    rodrick = RodrickAI()
    print(rodrick.think("What is reality?"))
    print(rodrick.recall("What is reality?"))
    print(rodrick.emotional_response("What is reality?"))
    rodrick.learn("What is reality?", 3)
    print(rodrick.recall("What is reality?"))
