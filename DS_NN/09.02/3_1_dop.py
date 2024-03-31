def taskOne(number):
    count = 0
    numString = str(number)

    for digit in numString:
        if digit != '0':
            count += 1

    return count

print(taskOne(1909))
