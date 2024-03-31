def taskA(sentense):
    cleaned = ' '.join(sentense.split())
    return cleaned.count(' ') + 1


def taskB(sentence):
    words = sentence.split()
    return ' '.join(reversed(words))


def taskC(sentence):
    return sentence.replace("1", "one")


print(taskA("     a     task     a      "))
print(taskB("car ride"))
print(taskC("car 1 ride"))

