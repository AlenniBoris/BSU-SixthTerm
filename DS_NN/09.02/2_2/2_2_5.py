def taskA(array):
    return array[::2]

def taskB(array):
    return [x for i, x in enumerate(array) if x > array[i - 1] and i != 0]

def taskD(array):
    minInd = array.index(min(array))
    maxInd = array.index(max(array))
    array[minInd], array[maxInd] = array[maxInd], array[minInd]


print('even numbers ', taskA([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print('greater numbers ', taskB([5, 1, 2, 3, 23, 23, 6, 7, 8, 9, 10]))

minMax = [1,2,3,4,5,6]
taskD(minMax)
print('min + max', minMax)