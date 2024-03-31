def taskA(cart, el):
    temp = list(cart[1])
    temp.append(el)
    return cart[0], temp


def taskB(cart, nums):
    return cart[0], cart[1], nums


def taskC(cart, expr):
    return cart[0], cart[1], expr


def taskD(cart):
    temp = list(cart[1])
    temp2 = list(temp)
    for el in temp:
        temp2.append(el)
    return cart[0], temp2


cartA = (1, [2, 3])
print('task A = ', taskA(cartA, 4))
print('task B = ', taskB(cartA, [4,5]))
print('task C = ', taskC(cartA, "abcd"))
print('task D = ', taskD(cartA))
