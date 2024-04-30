import numpy as np
import utilities
import prepared_data

x = prepared_data.data_letters_input_for_learning
y = prepared_data.data_letters_output_for_learning

np.random.seed(1)

syn0 = 2 * np.random.random((56, 8)) - 1
syn1 = 2 * np.random.random((8, 8)) - 1
syn2 = 2 * np.random.random((8, 29)) - 1

for iter in range(1000):
    l0 = x
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

l0 = np.array([utilities.flatten_2d_array(  [[0, 0, 1, 1, 0, 0, 0],
                                             [0, 0, 1, 1, 0, 0, 0],
                                             [1, 1, 1, 1, 1, 1, 1],
                                             [1, 1, 1, 1, 1, 1, 1],
                                             [1, 1, 1, 1, 1, 1, 1],
                                             [1, 1, 1, 1, 1, 1, 1],
                                             [1, 0, 0, 0, 0, 1, 0],
                                             [1, 0, 0, 0, 0, 1, 0]])])
l11 = np.dot(l0, syn0)
l1 = utilities.nonlin(l11)
l22 = np.dot(l1, syn1)
l2 = utilities.nonlin(l22)
l33 = np.dot(l2, syn2)
l3 = utilities.nonlin(l33)


print('Prognosis: \n', l3)

max_value = np.max(l3)
max_index = np.unravel_index(np.argmax(l3), l3.shape)
row_index = max_index[1]


print("\nMax value: ", max_value, " is letter number ", row_index)