def taskA(expr):
    word_count = {}
    words = expr.split()
    result = []
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 0
        result.append(word_count[word])
    return result


def taskB(synonyms, inputWord):
    for word, syn in synonyms.items():
        if word == inputWord:
            return syn
        elif syn == inputWord:
            return word
    return None


def taskC(text):
    word_counts = {}

    for line in text:
        words = line.split()
        for word in words:
            if word not in word_counts:
                word_counts[word] = 0
            count = word_counts[word]
            word_counts[word] = count + 1

    max_count = max(word_counts.values())
    frequent_words = [word for word, count in word_counts.items() if count == max_count]

    return min(frequent_words)


def taskD(text):
    lines = text.split("\n")
    freq = {}

    for line in lines[1:]:
        words = line.split()
        for word in words:
            freq[word] = freq.get(word, 0) + 1

    sortWords = sorted(freq.items(), key=lambda x: (-x[1], x[0]))

    return [word for word, freq in sortWords]


print('taskA = ', taskA("apple banana apple orange banana"))

print('task B = ')

word = "joyful"
synonyms = {
    "happy": "joyful",
    "good": "great",
    "sad": "unhappy"
}

synonym = taskB(synonyms, word)
if synonym:
    print(f"Синоним для слова '{word}' - '{synonym}'")
else:
    print(f"Синоним для слова '{word}' не найден.")

print('task C = ')
# Чтение строк текста
lines = ["apple banab babab orange", "orange babab kebab apple ", "orange apple aorans"]

# Поиск наиболее частого слова
result = taskC(lines)

# Вывод результата
print(result)

print('task D')

text = "6\napple banana apple orange apple orange\norange apple banana\nbanana apple orange apple"
sorted_words = taskD(text)
print(sorted_words)