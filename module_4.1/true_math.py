from math import inf
def divide(first, second):
    try:
        return int(first / second)
    except ZeroDivisionError:
        return inf
