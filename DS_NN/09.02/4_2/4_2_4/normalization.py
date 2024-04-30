def split_sentence(sentence):
    words = sentence.split()

    if len(words) > 5:
        words = words[:5]
    else:
        words += ['0'] * (5 - len(words))

    return words


def single_normalization(char):
    if char == "А" or char == "Б" or char == "В" or char == "Г" or char == "Д" or char == "Е" or char == "Ё" or\
            char == "Ж" or char == "З" or char == "И" or char == "Й" or char == "К" or char == "Л" or char == "М" or\
            char == "Н" or char == "О" or char == "П" or char == "Р" or char == "С" or char == "Т" or char == "У" or\
            char == "Ф" or char == "Х" or char == "Ц" or char == "Ч" or char == "Ш" or char == "Щ" or char == "Ъ" or\
            char == "Ы" or char == "Ь" or char == "Э" or char == "Ю" or char == "Я":
        return 1
    return 0


def normalize_word(word):
    if 'скидк' in word.lower() or 'распродаж' in word.lower():
        return 1
    value = 0
    for i in range(0, len(word)):
        value += single_normalization(word[i])
        if value > 1:
            return 0.5
    return 0


def normalize_sentence(sentence):
    words = split_sentence(sentence)
    normalized_sentence = []
    for i in range(0, len(words)):
        normalized_sentence.append(normalize_word(words[i]))
    return normalized_sentence