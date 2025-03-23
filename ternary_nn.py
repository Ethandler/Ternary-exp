import random
import numpy as np

class TernaryNeuralNetwork:
    """ A simple ternary neural network using balanced ternary weights (3,6,9). """

    def __init__(self, input_size, output_size):
        self.weights = np.random.choice([3, 6, 9], size=(input_size, output_size))
        self.biases = np.random.choice([3, 6, 9], size=(1, output_size))

    def activate(self, x):
        return np.where(x < 5, 3, np.where(x > 7, 9, 6))

    def forward(self, inputs):
        weighted_sum = np.dot(inputs, self.weights) + self.biases
        return self.activate(weighted_sum)

    def train(self, inputs, expected_output):
        predictions = self.forward(inputs)
        error = expected_output - predictions
        self.weights += np.random.choice([-3, 0, 3], size=self.weights.shape)
