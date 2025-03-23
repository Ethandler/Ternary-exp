import numpy as np
from quantum_ternary import QuantumTernary
import random

class TernaryNeuralNetwork:
    def __init__(self, input_size, output_size):
        self.qt = QuantumTernary()
        self.weights = self.random_ternary_weights((input_size, output_size))
        self.biases = self.random_ternary_weights((1, output_size))

    def random_ternary_weights(self, shape):
        arr = []
        for _ in range(shape[0] * shape[1]):
            arr.append(self.qt.measure())
        return np.array(arr).reshape(shape)

    def quantum_activate(self, x):
        activated = []
        for val in x.flatten():
            base = 3 if val < 5 else 9 if val > 7 else 6
            measure = self.qt.measure()
            final = random.choice([base, measure])
            activated.append(final)
        return np.array(activated).reshape(x.shape)

    def forward(self, inputs):
        weighted_sum = np.dot(inputs, self.weights) + self.biases
        return self.quantum_activate(weighted_sum)

    def train(self, inputs, expected_output):
        predictions = self.forward(inputs)
        error = expected_output - predictions
        self.weights += np.random.choice([-3, 0, 3], size=self.weights.shape)
        self.biases += np.random.choice([-3, 0, 3], size=self.biases.shape)
