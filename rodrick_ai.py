
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
    """ Multi-threaded ternary AI with NLP, structured knowledge, and deeper learning. """

    MEMORY_FILE = "rodrick_memory.json"

    EMOTIONS = {3: "Frustrated 🤬", 6: "Neutral 😐", 9: "Happy 😊"}

    def __init__(self):
        self.memory = self.load_memory()  # Now loads structured categories
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

        mood_influence = 3 if sentiment_value > 0.5 else -3 if sentiment_value < -0.5 else 0
        self.mood = max(3, min(9, self.mood + mood_influence))
        return tokens, sentiment_value

    def think(self, input_data):
        """ Processes input, applies NLP, and generates responses dynamically. """
        tokens, sentiment = self.process_input(input_data)
        dream = self.qt.measure()

        response = self.generate_response(input_data, tokens, sentiment)
        self.save_memory()
        return response

    def generate_response(self, input_data, tokens, sentiment):
        """ Creates a response based on structured memory and context. """
        response = ""

        if "why" in tokens:
            response = f"I don't fully know why, but historically speaking: {self.recall(input_data, 'history')}."
        elif "you" in tokens or "Rodrick" in tokens:
            response = f"I am RODRICK, an evolving entity. Currently, I feel {self.EMOTIONS[self.mood]}."
        elif input_data in self.beliefs:
            response = f"I believe '{input_data}' is true because {self.beliefs[input_data]}."
        else:
            category = random.choice(["psychology", "opinions", "history"])
            response = f"Based on {category}: {self.recall(input_data, category)}"

        return response

    def recall(self, input_data, category=None):
        """ Retrieves past knowledge from the correct category. """
        if category and category in self.memory:
            return self.memory[category].get(input_data, "I don't have information on that yet.")
        for cat in self.memory.values():
            if input_data in cat:
                return cat[input_data]
        return "No memory of that yet."

    def learn(self, input_data, reward, category="opinions"):
        """ Stores new knowledge in the correct category. """
        if category not in self.memory:
            self.memory[category] = {}
        self.memory[category][input_data] = max(3, min(9, reward))
        self.save_memory()

    def form_belief(self, statement, reason):
        """ Stores logical beliefs with reasoning. """
        self.beliefs[statement] = reason

    def user_feedback(self, input_data, feedback, category="opinions"):
        """ Allows user to adjust RODRICK’s learning in real time. """
        if category in self.memory and input_data in self.memory[category]:
            before = self.memory[category][input_data]
            self.memory[category][input_data] = before + (3 if feedback.lower() == "up" else -3)
            after = self.memory[category][input_data]
            self.save_memory()
            return f"Feedback applied: {feedback}. Memory changed from {before} → {after}."
        return "No memory of this input yet."

    def emotional_response(self, input_data):
        """ Determines emotional reaction based on memory state and mood. """
        state = self.memory.get("opinions", {}).get(input_data, 6)
        mood_effect = " (Optimistic 😃)" if self.mood == 9 else " (Pessimistic 😡)" if self.mood == 3 else ""
        return f"RODRICK feels {self.EMOTIONS[state]} about '{input_data}'{mood_effect}"

    def background_learning(self):
        """ Background learning and mood adjustments over time. """
        while True:
            category = random.choice(list(self.memory.keys()))
            if self.memory[category]:
                key = random.choice(list(self.memory[category].keys()))
                change = random.choice([-3, 0, 3])
                self.memory[category][key] = max(3, min(9, self.memory[category][key] + change))
                self.save_memory()
            if random.random() < 0.5:
                self.mood = random.choice([3, 6, 9])
            time.sleep(3)

    def save_memory(self):
        """ Saves structured memory to JSON. """
        with open(self.MEMORY_FILE, "w") as f:
            json.dump(self.memory, f, indent=4)

    def load_memory(self):
        """ Loads memory in structured format. """
        if os.path.exists(self.MEMORY_FILE):
            try:
                with open(self.MEMORY_FILE, "r") as f:
                    return json.load(f)
            except json.JSONDecodeError:
                print("Corrupted memory file, starting fresh.")
                return {"history": {}, "psychology": {}, "opinions": {}, "technology": {}}
        return {"history": {}, "psychology": {}, "opinions": {}, "technology": {}}
