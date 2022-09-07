import re


def calculator(numbers):
    if numbers == "":
        return 0

    alpha = []
    for i in numbers:
        if i.isalpha():
            alpha.append(ord(i) - 96)
    a = sum(alpha)
    numbers = map(int, re.findall(r"-?\d+", numbers))

    pos = []
    neg = []
    for i in numbers:
        if i < 0:
            neg.append(i)
        elif 1000 > i > 0:
            pos.append(i)
    if len(neg) > 0:
        raise Exception('negatives not allowed ' + str(neg))

    pos.append(a)
    return sum(pos);