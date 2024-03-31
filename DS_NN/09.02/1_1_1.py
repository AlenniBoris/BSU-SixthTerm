import math

# Функция сигмоиды
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

# Входные данные
I1 = 1
I2 = 0

# Веса
w1 = 0.45
w2 = 0.78
w3 = -0.12
w4 = 0.13
w5 = 1.5
w6 = -2.3

# Проход через скрытый слой
H1input = I1 * w1 + I2 * w3
H1output = sigmoid(H1input)

H2input = I1 * w2 + I2 * w4
H2output = sigmoid(H2input)

# Проход через выходной слой
O1input = H1output * w5 + H2output * w6
O1output = sigmoid(O1input)

# Ожидаемое значение
O1ideal = 1  # XOR(0, 1) = 1

# Вычисление ошибки MSE
error = ((O1ideal - O1output) ** 2) / 1

print("Результат:", O1output)
print("Ошибка:", error)
