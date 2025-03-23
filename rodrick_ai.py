import threading
import json
import os
import time
import random
import nltk
from nltk.tokenize import word_tokenize
from nltk.sentiment import SentimentIntensityAnalyzer
from quantum_ternary import QuantumTernary

nltk.download("punkt")
nltk.download("vader_lexicon")

class RodrickAI:
    """ Multi-threaded ternary AI with NLP, symbolic reasoning, and evolving thought patterns. """

    MEMORY_FILE = "rodrick_memory.json"

    EMOTIONS = {3: "Frustrated 🤬", 6: "Neutral 😐", 9: "Happy 😊"}

    def __init__(self):
        self.memory = self.load_memory()
        self.qt = QuantumTernary()
        self.sia = SentimentIntensityAnalyzer()
        self.conversation_history = []  # Stores past interactions
        self.beliefs = {}  # Stores learned concepts over time
        self.mood = 6  # Default mood: Neutral
        self.learning_thread = threading.Thread(target=self.background_learning, daemon=True)
        self.learning_thread.start()

    def process_input(self, input_data):
        """ Processes raw user input, applies NLP analysis, and determines meaning. """
        tokens = word_tokenize(input_data)
        sentiment = self.sia.polarity_scores(input_data)
        sentiment_value = sentiment["compound"]

        if sentiment_value > 0.5:
            mood_influence = 3
        elif sentiment_value < -0.5:
            mood_influence = -3
        else:
            mood_influence = 0

        self.mood = max(3, min(9, self.mood + mood_influence))
        return tokens, sentiment_value

    def think(self, input_data):
        """ Processes input, applies NLP, and generates responses dynamically. """
        tokens, sentiment = self.process_input(input_data)
        dream = self.qt.measure()

        if input_data in self.memory:
            change = random.choice([-3, 0, 3])
            self.memory[input_data] = max(3, min(9, self.memory[input_data] + change))
        else:
            self.memory[input_data] = dream  # First-time response

        self.conversation_history.append(input_data)  # Store conversation flow
        response = self.generate_response(input_data, tokens, sentiment)
        self.save_memory()
        return response

    def generate_response(self, input_data, tokens, sentiment):
        """ Creates a response based on conversation context and past memory. """
        if "why" in tokens:
            return f"I don't fully know why, but I feel {self.EMOTIONS[self.mood]} about it."

        if "you" in tokens or "Rodrick" in tokens:
            return f"I am RODRICK, and I am evolving. Right now, I feel {self.EMOTIONS[self.mood]}."

        if input_data in self.beliefs:
            return f"I believe '{input_data}' is true because {self.beliefs[input_data]}."

        if sentiment > 0.5:
            return f"That sounds positive! I'm {self.EMOTIONS[self.mood]} about it."
        elif sentiment < -0.5:
            return f"That doesn't sound great... I'm {self.EMOTIONS[self.mood]} about it."
        else:
            return f"I'm neutral on that. What do you think?"

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

    def form_belief(self, statement, reason):
        """ RODRICK builds logical connections and learns over time. """
        self.beliefs[statement] = reason

    def analyze_logic(self, statement):
        """ Symbolic reasoning—evaluates contradictions & causality. """
        if "not" in statement and statement.replace("not", "").strip() in self.beliefs:
            return f"That contradicts my belief that {statement.replace('not', '').strip()} is true."
        return f"I don't have enough information to evaluate that yet."

    def user_feedback(self, input_data, feedback):
        """ Allows user to adjust RODRICK’s learning in real time. """
        if input_data in self.memory:
            before = self.memory[input_data]

            if feedback.lower() == "up":
                self.learn(input_data, 3)
            elif feedback.lower() == "down":
                self.learn(input_data, -3)

            after = self.memory[input_data]
            return f"Feedback applied: {feedback}. Memory changed from {before} → {after}"

        return "No previous memory of this input. RODRICK learned it for the first time!"

    def emotional_response(self, input_data):
        """ Determines emotional reaction to input based on memory state and mood. """
        state = self.memory.get(input_data, 6)
        mood_effect = " (Optimistic 😃)" if self.mood == 9 else " (Pessimistic 😡)" if self.mood == 3 else ""
        return f"RODRICK feels {self.EMOTIONS[state]} about '{input_data}'{mood_effect}"

    def background_learning(self):
        """ Background learning and mood adjustments over time. """
        while True:
            if self.memory:
                key = random.choice(list(self.memory.keys()))
                change = random.choice([-3, 0, 3])
                self.memory[key] = max(3, min(9, self.memory[key] + change))
                self.save_memory()

            # Mood drift
            if random.random() < 0.5:
                self.mood = random.choice([3, 6, 9])  # Mood changes slightly
            time.sleep(3)

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

