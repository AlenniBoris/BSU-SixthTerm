#4.1.3
import numpy as np


def nonlin(x, deriv=False):
    if deriv:
        return x * (1 - x)

    return 1 / (1 + np.exp(-x))


X = np.array([[0, 0],
              [0, 1],
              [1, 0],
              [1, 1]])

# Output dataset for XOR
y = np.array([[0],
              [1],
              [1],
              [0]])

np.random.seed(1)

# randomly initialize our weights with mean 0
syn0 = 2 * np.random.random((2, 4)) - 1
syn1 = 2 * np.random.random((4, 1)) - 1

# Train the neural network
for j in range(60000):
    # Feed forward through layers 0, 1, and 2
    l0 = X
    l1 = nonlin(np.dot(l0, syn0))
    l2 = nonlin(np.dot(l1, syn1))

    # Calculate the error
    l2_error = y - l2

    if (j % 10000) == 0:
        print("Error: " + str(np.mean(np.abs(l2_error))))

    # Backpropagation
    l2_delta = l2_error * nonlin(l2, deriv=True)
    l1_error = l2_delta.dot(syn1.T)
    l1_delta = l1_error * nonlin(l1, deriv=True)

    # Update weights
    syn1 += l1.T.dot(l2_delta)
    syn0 += l0.T.dot(l1_delta)

print("\nOutput after training:")
print(l2)