def getSd(nummber):
    i = 2
    while i <= nummber:
        if nummber % i == 0:
            return i
        i += 1

def getDay(x, y):
    distance = x
    day = 1
    while distance < y:
        distance += distance * 0.1
        day += 1

    return day

def getYears(x, p, y):
    years = 0

    while x < y:
        x += x * (p / 100)
        x = int(x * 100) / 100
        years += 1

    return years

def fibonacci(a):
    if a == 0:
        return 0

    fib_prev = 0
    fib_curr = 1
    index = 1

    while fib_curr < a:
        fib_temp = fib_curr
        fib_curr += fib_prev
        fib_prev = fib_temp
        index += 1

    if fib_curr == a:
        return index
    else:
        return -1

print('Smallest Divisor:', str(getSd(49)))
print('Days Needed:', str(getDay(10, 200)))
print('Years Needed:', str(getYears(10, 10, 100)))
print('Index:', str(fibonacci(55)))