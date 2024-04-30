def taskA(first, second):
    return len(set(first).intersection(set(second)))


def taskB(expr):
    numbers = set()
    sequence = expr.split()
    result = []
    for num in sequence:
        if num in numbers:
            result.append("YES")
        else:
            result.append("NO")
            numbers.add(num)
    for word in result:
        print(word)


def taskC(Ania_colors, Borya_colors):
    Ania_set = set(Ania_colors)
    Borya_set = set(Borya_colors)
    both_sets = Ania_set.intersection(Borya_set)
    Ania_only = Ania_set.difference(Borya_set)
    Borya_only = Borya_set.difference(Ania_set)

    return both_sets, Ania_only, Borya_only


print('task A = ', taskA([1,2,3,4,5], [2,4,7,8]))

expr = "1 2 3 2 4 3 5"
print('task B = ', expr)
taskB(expr)
print()

print('taskC')

Ania_colors = [1, 3, 5, 7, 9]
Borya_colors = [1, 2, 4, 6, 8, 9]

both_sets, Ania_only, Borya_only = taskC(Ania_colors, Borya_colors)

print(len(both_sets))
print(*sorted(both_sets))

print(len(Ania_only))
print(*sorted(Ania_only))

print(len(Borya_only))
print(*sorted(Borya_only))

