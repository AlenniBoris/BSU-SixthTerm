import numpy as np
import prepairing_data
import utilities

data = prepairing_data.data_task_1

X = np.empty((0, 4), dtype=float)
y = np.array([], dtype=float)

for i in range(len(data) - 4):
    array_to_append = np.array(data[i: i + 4], dtype=float)
    X = np.append(X, [array_to_append], axis=0)
    y = np.append(y, data[i + 4])

y = y.reshape((len(X), 1))

np.random.seed(1)

syn0 = 2 * np.random.random((4, 2)) - 1
syn1 = 2 * np.random.random((2, 4)) - 1
syn2 = 2 * np.random.random((4, 1)) - 1

for iter in range(6000):
    l0 = X
    l1 = utilities.nonlin(np.dot(l0, syn0))
    l2 = utilities.nonlin(np.dot(l1, syn1))
    l3 = utilities.nonlin(np.dot(l2, syn2))

    l3_error = y - l3
    l3_delta = l3_error * utilities.nonlin(l3, True)

    l2_error = l3_delta.dot(syn2.T)
    l2_delta = l2_error * utilities.nonlin(l2, True)

    l1_error = l2_delta.dot(syn1.T)
    l1_delta = l1_error * utilities.nonlin(l1, True)

    syn2 += l2.T.dot(l3_delta)
    syn1 += l1.T.dot(l2_delta)
    syn0 += l0.T.dot(l1_delta)


l0 = [1.9542, 1.9509, 1.9509, 1.9509]
l11 = np.dot(l0, syn0)
l1 = utilities.nonlin(l11)
l22 = np.dot(l1, syn1)
l2 = utilities.nonlin(l22)
l33 = np.dot(l2, syn2)
l3 = utilities.nonlin(l33)

print('Prognosis: ', utilities.inverse_nonlin(l3))
print("Error:", (utilities.nonlin(1.9548) - l3))