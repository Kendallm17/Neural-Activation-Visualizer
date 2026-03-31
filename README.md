

## Overview

The **Neural Activation Visualizer** is an interactive project designed to explore and understand how different activation functions behave in neural networks.

This project focuses on building intuition about **non-linearity**, one of the core concepts in deep learning. By visualizing activation functions, users can see how neural networks transform input data and why activation functions are essential for learning complex patterns.

---

## Objectives

* Understand the role of activation functions in neural networks
* Visualize how inputs are transformed into outputs
* Compare different activation functions
* Build intuition for concepts like **saturation** and **vanishing gradients**

---

## Concepts Covered

* Linear vs Non-linear transformations
* Activation functions:

  * Identity
  * Sigmoid
  * ReLU
  * Softmax (optional extension)
* Saturation
* Vanishing Gradient (introductory level)

---

## Technologies Used

* **Python**
* **NumPy** (numerical computations)
* **Matplotlib** (visualization)

*(Optional for advanced version)*

* **Streamlit** or **Plotly** (interactive UI)

---

## Features

* Plot multiple activation functions on the same graph
* Compare behavior across input ranges
* Visualize how functions respond to extreme values
* (Optional) Interactive sliders for input manipulation
* (Optional) Simulate a simple neuron:

  * Input → Weight → Bias → Activation

---

## Activation Functions Implemented

* **Identity**: Linear transformation (no learning power)
* **Sigmoid**: Outputs values between 0 and 1 (probabilistic interpretation)
* **ReLU (Rectified Linear Unit)**: Efficient and widely used in deep learning

---

## Example Output

The visualizer generates plots that show how each activation function behaves over a range of input values (e.g., -10 to 10), helping users understand:

* Where functions saturate
* How gradients behave
* Why non-linearity is critical

---

## Project Structure

```
neural-activation-visualizer/
│
├── main.py             # Main script to run visualizations
├── activations.py      # Activation function definitions
├── utils.py            # Helper functions (optional)
├── README.md
```

---

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/your-username/neural-activation-visualizer.git
```

2. Navigate into the project:

```bash
cd neural-activation-visualizer
```

3. Install dependencies:

```bash
pip install numpy matplotlib
```

4. Run the project:

```bash
python main.py
```

---


## Why This Project Matters

Understanding activation functions is essential to understanding **how neural networks learn**. Without non-linearity, deep learning models would collapse into simple linear functions.

This project builds the foundation for:

* Backpropagation
* Gradient descent
* Deep neural networks

---

## Author

Kendall Chinchilla Araya

---

This project is for educational purposes.
