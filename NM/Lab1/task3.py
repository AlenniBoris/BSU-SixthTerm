import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt


# Заданные функции
def f1(x):
    return pow(x, 2) * np.cos(3 * x - 1)


def f2(x):
    return np.abs(x * np.abs(x) - 1)


# Функция для построения интерполяционного кубического сплайна
def cubic_spline_interpolation(x, y, d2y_start, d2y_end):
    cs = CubicSpline(x, y, bc_type=((2, d2y_start), (2, d2y_end)))
    return cs


def startProgr(min, max, degree):
    valuesX = np.linspace(min, max, degree)
    valuesF1 = [f1(value) for value in valuesX]
    valuesF2 = [f2(value) for value in valuesX]
    return valuesX, valuesF1, valuesF2

# Заданные узлы для интерполяции
xmin, xmax = -2, 2
degrees = [2, 4, 8, 16]

# Для каждой функции

for degree in degrees:

    valuesX, valuesF1, valuesF2 = startProgr(xmin, xmax, degree+1)
    # Значения вторых производных на границах

    d2y_f1_start = f1(valuesX[1]) - 2 * f1(valuesX[0]) + f1(valuesX[1])
    d2y_f1_end = f1(valuesX[-2]) - 2 * f1(valuesX[-1]) + f1(valuesX[-2])

    d2y_f2_start = f2(valuesX[1]) - 2 * f2(valuesX[0]) + f2(valuesX[1])
    d2y_f2_end = f2(valuesX[-2]) - 2 * f2(valuesX[-1]) + f2(valuesX[-2])

    # Построение интерполяционного кубического сплайна
    cs_f1 = cubic_spline_interpolation(valuesX, valuesF1, d2y_f1_start, d2y_f1_end)
    cs_f2 = cubic_spline_interpolation(valuesX, valuesF2, d2y_f2_start, d2y_f2_end)

    # Оценка значений сплайна на более широком диапазоне для построения графика
    lineValuesX = np.linspace(xmin, xmax, 500)
    y_interp_f1 = cs_f1(lineValuesX)
    y_interp_f2 = cs_f2(lineValuesX)

    # Построение графиков
    # График для f1(x)
    plt.subplot(2, 2, 1)
    lineValuesX = np.linspace(xmin, xmax, 500)
    plt.plot(lineValuesX, [f1(x) for x in lineValuesX], label='f1(x)')
    plt.plot(lineValuesX, y_interp_f1, label='Интерп. мн-н Ньютона для f1(x)')
    plt.title('f1(x)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)

    # График для f2(x)
    plt.subplot(2, 2, 2)
    plt.plot(lineValuesX, [f2(x) for x in lineValuesX], label='f2(x)')
    plt.plot(lineValuesX, y_interp_f2, label='Интерп. мн-н Ньютона для f2(x)')
    plt.title('f2(x)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.show()
