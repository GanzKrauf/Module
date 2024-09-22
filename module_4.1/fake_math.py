def divide(first, second):
    a = int(first)
    b = int(second)
    try:
        return a / b
    except ZeroDivisionError:
        return 'Ошибка'
