import math

import numpy as np

def f(x):
    return np.exp(x) / np.sqrt(1 - x**2)

def NAST(func, a, b, n):
    sum_result = 0
    for i in range(n + 1):
        sum_result += func(np.cos(np.pi * (2 * i + 1) / (2 * (n + 1))))
    return sum_result * np.pi / (n + 1)

def RECTANGLE(func, a, b, n):
    h = (b - a) / n
    sum_result = 0
    for i in range(n):
        sum_result += func(a + i * h + h / 2)
    return h * sum_result


a = -1
b = 1
num_nodes = [20,40,200,1000,10000,100000]

print("real = ", 3.97746)
print("Number of Nodes\tNAST\tRectangle Formula")
for num in num_nodes:
    print("number = ", num)
    for n in range(1, num + 1):
        nastRes = NAST(f, a, b, n)
        rectRes = RECTANGLE(f, a, b, n)
        print(f"{n}\t\t{nastRes}\t{rectRes}")
    print()