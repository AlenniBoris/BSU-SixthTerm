from _pydecimal import Decimal


def lastDigit(number):
    return number%10

def fractional(x):
    decimal_x = Decimal(str(x))
    fractional_part = decimal_x - Decimal(int(x))
    return fractional_part

def firstDecimal(x):
    return int(fractional(x) * 10)

def round(x):
    intPart = int(x)
    fractPart = fractional(x)

    if fractPart >= 0.5:
        return intPart + 1
    else:
        return intPart


print('Last Digit:', lastDigit(12))
print('Fractional Part:', fractional(12.312321312))
print('First Decimal Digit:', firstDecimal(12.312321312))
print('Rounded:', round(12.512321312))