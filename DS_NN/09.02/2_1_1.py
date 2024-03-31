def getMaxOfThree(a, b, c):
    return max(a, b, c)

def equalNumbers(a, b, c):
    if a == b == c:
        return 3
    elif a == b or a == c or b == c:
        return 2
    else:
        return 0

def leapYear(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def movingRook(startCol, startRow, endCol, endRow):
    if (int(startCol) < 0 or int(startCol) > 8) or (int(startRow) < 0 or int(startRow) > 8) or (int(endCol) < 0 or int(endCol) > 8) or (int(endRow) < 0 or int(endRow) > 8):
        return "NO"
    if startCol == endCol or startRow == endRow:
        return "YES"
    else:
        return "NO"

a = input("Enter a: ")
b = input("Enter b: ")
c = input("Enter c: ")

print(getMaxOfThree(a, b, c))
print(equalNumbers(a, b, c))

year = input("Enter year: ")
print(leapYear(int(year)))

startCol = input("Enter start column : ")
startRow = input("Enter start row: ")
endCol = input("Enter end column: ")
endRow = input("Enter end row: ")

print(movingRook(startCol, startRow, endCol, endRow))