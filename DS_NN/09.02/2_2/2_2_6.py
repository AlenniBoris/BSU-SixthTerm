def taskA(sentence):
    vowels = 'aeiouAEIOU'
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    vCounter = 0
    cCounter = 0

    for char in sentence:
        if char in vowels:
            vCounter += 1
        elif char in consonants:
            cCounter += 1

    return vCounter, cCounter


def taskC(sentence):
    frequency = {}

    for letter in sentence:
        if letter.isalpha():
            if letter in frequency:
                frequency[letter] += 1
            else:
                frequency[letter] = 1

    return frequency


def taskB(sentence):
    words = sentence.split()
    result = []
    for word in words:
        capitalized_word = word.capitalize() + "."
        result.append(capitalized_word)

    capitalized_sentence = ' '.join(result)
    return capitalized_sentence


def taskD(sentence):
    words = sentence.split()
    count = 0

    for word in words:
        if len(word) > 0 and word[0].lower() == word[-1].lower():
            count += 1

    return count


def taskF(array):
    nums = [x for x in array if x != 0]
    zeros = [x for x in array if x == 0]
    return nums + zeros


def taskG(array):
    return [x for i, x in enumerate(array) if i % 2 == 0 and x > 0]


print("task A ", taskA("aabbaa"))

frequency = taskC("Hello, World!")
for letter, count in frequency.items():
    print(f"{letter}: {count}")

print("task B", taskB("hello world Sun."))
print("task D", taskD("aba ndnd aita"))
print("task F", taskF([1,0,0,0,2,2,0,0,0]))
print("task G", taskG([1,0,0,0,2,3,0,0,0]))