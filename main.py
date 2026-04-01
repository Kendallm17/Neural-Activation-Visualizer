"""
main.py

This is the main file that runs the visualization.

It generates input values and plots different activation functions
to compare their behavior.
"""

import numpy as np
import matplotlib.pyplot as plt

# Import activation functions from activations.py
from activations import identity, sigmoid, relu


def generate_input(start=-10, end=10, num=100):
    """
    Generates a range of input values.

    Parameters:
        start (int): Starting value
        end (int): Ending value
        num (int): Number of points

    Returns:
        np.array: Evenly spaced values
    """
    return np.linspace(start, end, num)


def plot_activations(x):
    """
    Plots multiple activation functions on the same graph.

    Parameters:
        x (np.array): Input values
    """

    # Compute outputs
    y_identity = identity(x)
    y_sigmoid = sigmoid(x)
    y_relu = relu(x)

    # Plot each function
    plt.plot(x, y_identity, label="Identity")
    plt.plot(x, y_sigmoid, label="Sigmoid")
    plt.plot(x, y_relu, label="ReLU")

    # Graph details
    plt.title("Activation Functions Visualization")
    plt.xlabel("Input")
    plt.ylabel("Output")

    plt.legend()
    plt.grid()

    plt.show()


if __name__ == "__main__":
    # Generate input values
    x = generate_input()

    # Plot activation functions
    plot_activations(x)