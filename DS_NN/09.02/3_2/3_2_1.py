import math

def taskA(firstX,firstY,secondX,secondY):
    if (firstX is None) or (firstY is None) or (secondX is None) or (secondY is None):
        raise RuntimeError("Enter nothing")
    try:
        fX = float(firstX)
        fY = float(firstY)
        sX = float(secondX)
        sY = float(secondY)
        return math.sqrt(pow(fX-sX,2)+pow(fY-sY,2))
    except ValueError:
        raise ValueError("Invalid input: not a number")


def taskB(a,n):
    res = 1
    for num in range(0,n):
        res *= a

    return res


def capitalize(word):
    return word[0].upper() + word[1:]


def taskC(sentence):
    words = sentence.split()
    result = [capitalize(word) for word in words]
    result = ' '.join(result)
    return result


def taskD(a,b):
    return max(a,b)


print('task A = ', taskA(1,4,5,5))
print('task B = ', taskB(4,4))
print('task C = ', taskC("apple banana cucumber"))
print('task D = ', taskD(15,25))
print('task E')
# print('task A = ', taskA("1,4,5,5","dhhdhd","djdjdj","hdhd"))
# print('task A = ', taskA(None,None,None,None))
