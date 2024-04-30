import math

def sigmoid(x):
    return 1 / (1 + math.exp(-1 * x))

def floor(x, size):
    return float(str(x)[:(size + 2)])

i = (1, 0)
sets = [[0.45, 0.78, -0.12, 0.13, 1.5, -2.3],[0,1,0.31,0,1,0.13,1.5,1],[0,0,0.31,0,1,0.13,1.5,1],[1,1,0.31,0,1,0.13,1.5,1]]

def calc(w, i):
    # Проход через скрытый слой
    H1input = i[0] * w[0] + i[1] * w[2]
    H1output = sigmoid(H1input)

    H2input = i[0] * w[1] + i[1] * w[3]
    H2output = sigmoid(H2input)

    # Проход через выходной слой
    O1input = H1output * w[4] + H2output * w[5]
    O1output = sigmoid(O1input)

    # Ожидаемое значение
    O1ideal = 1  # XOR(0, 1) = 1

    # Вычисление ошибки MSE
    error = ((O1ideal - O1output) ** 2) / 1

    return O1output,error

o1,err1 = calc(sets[0],i)
o2,err2 = calc(sets[1],i)
o3,err3 = calc(sets[2],i)
o4,err4 = calc(sets[3],i)

print("Результат:",o1)
print("Ошибка:",err1)
print("\n")

print("Результат:",o2)
print("Ошибка:",err2)
print("\n")

print("Результат:",o3)
print("Ошибка:",err3)
print("\n")

print("Результат:",o4)
print("Ошибка:",err4)
print("\n")

print(sum((err1,err2,err3,err4))/4)

