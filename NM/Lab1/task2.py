import numpy as np
import matplotlib.pyplot as plt


# Заданные функции
def f1(x):
    return pow(x, 2) * np.cos(3 * x - 1)


def f2(x):
    return np.abs(x * np.abs(x) - 1)


def chebyshev(min, max, degree):
    nodes = np.zeros(degree)
    for i in range(degree):
        nodes[i] = 0.5 * (xmin + xmax) + 0.5 * (xmax - xmin) * np.cos((2 * i + 1) * np.pi / (2 * degree))
    return nodes

# Вычисление разделённых разностей
def divided_diff(x, y):
    n = len(x)
    coef = np.zeros([n, n])
    coef[:, 0] = y

    for j in range(1, n):
        for i in range(n - j):
            coef[i][j] = (coef[i + 1][j - 1] - coef[i][j - 1]) / (x[i + j] - x[i])

    return coef[0]


# Построение интерполяционного многочлена Ньютона
def newton(x, y):
    coef = divided_diff(x, y)
    n = len(x)
    t = chebyshev(min(x), max(x), 1000)
    result = np.zeros_like(t)

    for i in range(n):
        term = coef[i]
        for j in range(i):
            term *= (t - x[j])
        result += term

    return t, result


def startProgr(min, max, degree):
    valuesX = chebyshev(min, max, degree)
    valuesF1 = [f1(value) for value in valuesX]
    valuesF2 = [f2(value) for value in valuesX]
    return valuesX, valuesF1, valuesF2


def printRes(function, newton, number):
    print(function + ": ")
    print(newton.evalf(n=number))


def create_polynomial(x, y):
    coef = divided_diff(x, y)
    if len(x) == 3:
        print("\nAnalytical representation of the 2nd-degree polynomial:")
        print(f"{coef[0]:.3f} + {coef[1]:.3f} * (x - {x[0]:.3f}) + {coef[2]:.3f} * (x - {x[0]:.3f}) * (x - {x[1]:.3f})")
    return lambda point: sum(coef[i] * np.prod(point - x[:i]) for i in range(len(x)))



xmin, xmax = -2, 2
degrees = [2, 4, 8, 16]

for degree in degrees:
    print(f"Степень интерполяции n = {degree}:")

    # Узлы интерполяции
    valuesX, valuesF1, valuesF2 = startProgr(xmin, xmax, degree+1)

    # Построение интерполяционного многочлена Ньютона для f1(x)
    t_f1, newtonF1 = newton(valuesX, valuesF1)
    t_f2, newtonF2 = newton(valuesX, valuesF2)

    if degree == 2:
        print('f1 = ')
        create_polynomial(valuesX, valuesF1)
        print('f2 = ')
        create_polynomial(valuesX, valuesF2)

        # Построение графиков для многочленов каждой степени
    plt.figure(figsize=(10, 6))

    # График для f1(x)
    plt.subplot(2, 2, 1)
    plt.plot(t_f1, f1(t_f1), label='f1(x)')
    plt.plot(t_f1, newtonF1, label='Интерп. мн-н Ньютона для f1(x)')
    plt.title('f1(x)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)

    # График для f2(x)
    plt.subplot(2, 2, 2)
    plt.plot(t_f2, f2(t_f2), label='f2(x)')
    plt.plot(t_f2, newtonF2,label='Интерп. мн-н Ньютона для f2(x)')
    plt.title('f2(x)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.show()