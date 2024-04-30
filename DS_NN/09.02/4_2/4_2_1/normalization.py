
def mass_normalization(value):
    if value <= 0.5:
        return 0
    elif 0.5 <= value < 1:
        return 0.25
    elif 1 <= value < 2:
        return 0.5
    elif 2 <= value < 5:
        return 0.75
    return 1


def power_normalization(value):
    if value <= 20:
        return 0
    elif 20 < value <= 50:
        return 0.25
    elif 50 < value <= 100:
        return 0.5
    elif 100 < value <= 200:
        return 0.75
    return 1


def passengers_normalization(value):
    if value <= 2:
        return 0
    elif 2 < value <= 5:
        return 0.25
    elif 5 < value <= 10:
        return 0.5
    elif 10 < value <= 20:
        return 0.75
    return 1


def lifting_capacity_normalization(value):
    if value <= 1:
        return 0
    elif 1 < value <= 2:
        return 0.25
    elif 2 < value <= 3:
        return 0.5
    elif 3 < value <= 4:
        return 0.75
    return 1