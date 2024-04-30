import numpy as np
import normalization
import utilities

data_task_1 = utilities.nonlin(np.array([1.9585, 1.9585, 1.9585, 1.9666, 1.9707, 1.9653, 1.9538, 1.9538, 1.9538, 1.9597, 1.9640, 1.9697, 1.9542,
               1.9509, 1.9509, 1.9509]))


data_cars_input_for_learning = np.array([[normalization.mass_normalization(0.645), normalization.power_normalization(33), normalization.passengers_normalization(4), normalization.lifting_capacity_normalization(0.34)],
                                         [normalization.mass_normalization(2.880), normalization.power_normalization(152), normalization.passengers_normalization(14), normalization.lifting_capacity_normalization(1.5)],
                                         [normalization.mass_normalization(1.110), normalization.power_normalization(88), normalization.passengers_normalization(5), normalization.lifting_capacity_normalization(0.475)],
                                         [normalization.mass_normalization(10.400), normalization.power_normalization(260), normalization.passengers_normalization(3), normalization.lifting_capacity_normalization(6)],
                                         [normalization.mass_normalization(2.880), normalization.power_normalization(152), normalization.passengers_normalization(3), normalization.lifting_capacity_normalization(1.5)],
                                         [normalization.mass_normalization(9.895), normalization.power_normalization(122), normalization.passengers_normalization(30), normalization.lifting_capacity_normalization(6.2)],
                                         [normalization.mass_normalization(3.695), normalization.power_normalization(136), normalization.passengers_normalization(3), normalization.lifting_capacity_normalization(3)],
                                         [normalization.mass_normalization(2.170), normalization.power_normalization(116), normalization.passengers_normalization(5), normalization.lifting_capacity_normalization(0.6)],
                                         [normalization.mass_normalization(27.895), normalization.power_normalization(278), normalization.passengers_normalization(150), normalization.lifting_capacity_normalization(11)]])


data_cars_output_for_learning = np.array([[1, 0, 0],
                                          [0, 1, 0],
                                          [1, 0, 0],
                                          [0, 0, 1],
                                          [0, 0, 1],
                                          [0, 1, 0],
                                          [0, 0, 1],
                                          [1, 0, 0],
                                          [0, 1, 0]])


data_cars_input_test = np.array([[normalization.mass_normalization(74), normalization.power_normalization(1050), normalization.passengers_normalization(1), normalization.lifting_capacity_normalization(90)],
                                 [normalization.mass_normalization(13.6), normalization.power_normalization(260), normalization.passengers_normalization(10), normalization.lifting_capacity_normalization(3)],
                                 [normalization.mass_normalization(0.3), normalization.power_normalization(40), normalization.passengers_normalization(3), normalization.lifting_capacity_normalization(0.25)],
                                 [normalization.mass_normalization(0.2), normalization.power_normalization(1), normalization.passengers_normalization(4), normalization.lifting_capacity_normalization(0.2)],
                                 [normalization.mass_normalization(0.02), normalization.power_normalization(0.3), normalization.passengers_normalization(1), normalization.lifting_capacity_normalization(0.1)],
                                 [normalization.mass_normalization(18.4), normalization.power_normalization(245), normalization.passengers_normalization(168), normalization.lifting_capacity_normalization(12)]])