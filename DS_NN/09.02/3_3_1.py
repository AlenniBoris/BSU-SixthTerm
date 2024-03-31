def taskA(last_names, file_name):
    with open(file_name, "w") as file:
        for last_name in last_names:
            file.write(last_name + "\n")


def taskB(file_name):
    with open(file_name, "r") as file:
        for idx, line in enumerate(file, start=1):
            print(str(idx), line.strip())


def taskC(last_names, names, file_name):
    with open(file_name, "w") as file:
        for last_name, name in zip(last_names, names):
            file.write(last_name + " " + name + "\n")


def taskD(file_name):
    with open(file_name, "r") as file:
        for idx, line in enumerate(file, start=1):
            strings = str(line).split(" ")
            print(str(idx), strings[0], strings[1][0] + ".")


last_names = ["Аленников", "Видевич", "Гатальский", "Кондратьев"]
names = ["Борис", "Саша", "Антон", "Женя"]

taskA(last_names, "group.txt")
print()
taskB("group.txt")
print()
taskC(last_names, names, "group_with_names.txt")
print()
taskD("group_with_names.txt")