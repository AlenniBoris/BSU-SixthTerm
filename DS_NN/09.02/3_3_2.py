import math
import random
import math_module


def taskA():
    return math.log2(15)


def taskB():
    random.seed(50)
    return random.uniform(0,1)


def taskC():
    a = 10
    b = 12
    print(dir())

print("task A")
print(taskA())

print('taskB')
for _ in range(0,4):
    print(taskB())


print('task D')
print(math_module.log_base_a(1000,10))

print('task C')
taskC()