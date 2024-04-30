import numpy as np
import matplotlib.pyplot as plt


# Определение функций для системы уравнений
def f(x, y):
    U, V = y
    return np.array([U * V + x - 1, np.sqrt(U ** 2 + 1) - V])


def display(x_values, y_values, title):
    u_values = y_values[:, 0]
    v_values = y_values[:, 1]
    plt.figure(figsize=(10, 6))
    plt.plot(x_values, u_values, label='u(x)')
    plt.plot(x_values, v_values, label='v(x)')
    plt.title(title)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()


# Явный метод Эйлера
def euler_method(f, h, y0, x_values):
    y_values = np.zeros((len(x_values), len(y0)))
    y_values[0] = y0
    for i in range(1, len(x_values)):
        xi = x_values[i]
        yi = y_values[i-1]
        yi_temp = yi + h*f(xi, yi)
        y_values[i] = yi_temp

    return x_values, y_values


# Метод Рунге-Кутта 2-го порядка
def runge_kutta_2nd_order(f, h, y0, x_values):
    y_values = np.zeros((len(x_values), len(y0)))
    y_values[0] = y0
    for i in range(1, len(x_values)):
        xi = x_values[i]
        yi = y_values[i - 1]
        phi0 = f(xi, yi)
        phi1 = f(xi + h/2, yi + (h/2)*phi0)
        yi_temp = yi + h * phi1
        y_values[i] = yi_temp

    return x_values, y_values


# Начальные условия
startData = np.array([1.5, 0.75])
h = 1e-4
x_range = [1, 2]
N = int((x_range[1] - x_range[0]) / h)
x_values = np.linspace(x_range[0], x_range[1], N + 1)

# Вычисление решений методом Эйлера
x_euler, y_euler = euler_method(f, h, startData, x_values)
# Вычисление решений методом Рунге-Кутта 2-го порядка
x_rk2, y_rk2 = runge_kutta_2nd_order(f, h, startData, x_values)

# Построение графиков
display(x_euler, y_euler,"Эйлер")
display(x_rk2, y_rk2, "Рунге")

y1 = y_euler[-1]
y2 = y_rk2[-1]
print("Модуль разности решений в крайней правой точке интервала: ", abs(y1-y2))


