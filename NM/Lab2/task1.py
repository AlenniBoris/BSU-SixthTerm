import math

def function(x):
    return math.log(math.pow(x,2)+1)

def indefinite_integral(x):
    return x*math.log(math.pow(x,2)+1)-2*x+2*math.atan(x)

def integral(a,b):
    return indefinite_integral(b)-indefinite_integral(a)


def trapecia(a,b,n):
    h = (b - a) / n
    result = 0.5 * (function(a) + function(b))
    for i in range(1, n):
        result += function(a + i * h)
    result *= h
    return result

def process(a, b, epsilon):
    n = 1
    prev = trapecia(a, b, n)
    while True:
        n *= 2
        result = trapecia(a, b, n)
        if abs(result - prev) < epsilon:
            return result, (b - a) / n
        prev = result


a = 0
b = 1
epsilon = math.pow(10,-6)


print('Реальное значение',integral(a,b))

calculated, step = process(a,b,epsilon)

print('шаг ', step)
print('вычисленное ', calculated)
