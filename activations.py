"""
activations.py

This file contains implementations of common activation functions
used in neural networks.

Each function takes a NumPy array (or scalar) as input
and returns the transformed output.
"""
import numpy as np

def identity(x):
    """
    Identity activation function.

    f(x) = x

    This function does not introduce non-linearity.
    It is mainly used for understanding purposes.

    Parameters:
        x (float or np.array): Input value(s)

    Returns:
        Same as input
    """
    return x

def sigmoid(x):
    """
    Sigmoid activation function.

    f(x) = 1 / (1 + e^(-x))

    Output range: (0, 1)

    Used for probabilistic interpretation.
    Suffers from saturation (vanishing gradient).

    Parameters:
        x (float or np.array): Input value(s)

    Returns:
        np.array: Transformed values
    """
    return 1 / (1 + np.exp(-x))

def relu(x):
    """
    ReLU (Rectified Linear Unit) activation function.

    f(x) = max(0, x)

    - Outputs 0 for negative inputs
    - Linear for positive inputs

    Helps mitigate vanishing gradient problem.

    Parameters:
        x (float or np.array): Input value(s)

    Returns:
        np.array: Transformed values
    """
    return np.maximum(0, x)

 def softmax(x):
    """
    Softmax activation function.

    Converts a vector into probabilities that sum to 1.

    f(x_i) = e^(x_i) / sum(e^(x_j))

    Used in multi-class classification.

    Parameters:
        x (np.array): Input vector

    Returns:
        np.array: Probability distribution
    """
    exp_x = np.exp(x - np.max(x))  # for numerical stability
    return exp_x / np.sum(exp_x)   

