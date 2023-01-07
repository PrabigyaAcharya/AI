import numpy as np
import math
from random import random


class MLP:

    def __init__(self, num_inputs=2, num_hidden_layers=[3, 5], num_outputs=1):
        self.num_inputs = num_inputs
        self.num_hidden_layers = num_hidden_layers
        self.num_outputs = num_outputs

        layers = [self.num_inputs] + \
            self.num_hidden_layers + [self.num_outputs]

        self.weights = []
        for i in range(len(layers)-1):
            w = np.random.rand(layers[i], layers[i+1])
            self.weights.append(w)

        # each array in the list represent activation value
        activations = []
        for i in range(len(layers)):
            a = np.zeros(layers[i])
            activations.append(a)

        self.activations = activations

        derivatives = []
        for i in range(len(layers)-1):  # number of weights matrices sanga equal
            d = np.zeros((layers[i], layers[i+1]))
            derivatives.append(d)

        self.derivatives = derivatives

    def _sigmoid(self, x):
        return 1/(1+np.exp(-x))

    def _sigmoid_derivative(self, x):
        # return (self._sigmoid(x) + self._sigmoid(1-x))
        # as the sigmoid is the activation fucntion itself
        return (x*(1.0-x))

    def mse(self, target, output):
        return np.average((target-output)**2)

    def forward_propagate(self, inputs):

        activations = inputs

        self.activations[0] = inputs

        for i, w in enumerate(self.weights):
            net_inputs = np.dot(activations, w)
            activations = self._sigmoid(net_inputs)
            self.activations[i+1] = activations

        return activations

    def back_propagate(self, error):

        for i in reversed(range(len(self.derivatives))):
            activations = self.activations[i+1]
            delta = error * self._sigmoid_derivative(activations)

            # make it suitable for mat mult
            current_activations = self.activations[i]
            current_activations_reshaped = current_activations.reshape(
                current_activations.shape[0], -1)

            delta_reshaped = delta.reshape(delta.shape[0], -1).T

            self.derivatives[i] = np.dot(
                current_activations_reshaped, delta_reshaped)

            error = np.dot(delta, self.weights[i].T)

           # print(f"Derivatives for W{i} = {self.derivatives[i]}")
        return error

    def gradient_descent(self, learning_rate):
        for i in range(len(self.weights)):
            weights = self.weights[i]
            derivatives = self.derivatives[i]
#            print(f"Original Weights{i}:{weights}")
            weights += derivatives * learning_rate
#            print(f"Updated Weights{i}:{weights}")

    def train(self, inputs, targets, epochs, learning_rate):
        
        for i in range(epochs):
            sum_error = 0
            for (input, target) in zip(inputs, targets):
                # propagate forward
                output = self.forward_propagate(input)
                # calculate error
                error = target-output
                # back propagation
                self.back_propagate(error)
                # gradient descent
                self.gradient_descent(learning_rate)
                #epoch error
                sum_error+=self.mse(target, output)
            print(f"Error at epoch {i} = {sum_error/len(inputs)}")

# create mlp
mlp = MLP(2, [5], 1)

# create inputs
inputs = np.array([[random()/2 for i in range(2)] for j in range(1000)])
targets = np.array([[i[0]+i[1]]for i in inputs])

mlp.train(inputs, targets, 50, 0.1)

for i in range(5):
    check = np.array([random()/2 for i in range(2)])
    x, y = tuple(check)
    output = mlp.forward_propagate(check)
    print(f"Prediction: {x} + {y} = {output}")
