def dopB(string):
    words = string.split()
    names = [word for word in words if word[0].isupper()]
    result = sorted(names)
    return result

sentence = "Boris Anon topping"
print("B :" , sentence)
print('dopB = ', dopB(sentence))