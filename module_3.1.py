calls = 0


def caunt_calls():
    global calls
    calls += 1


def string_info(string):
    caunt_calls()
    num = 0
    for i in string:
        a = string.upper()
        b = string.lower()
        num += len(i)
    return num, a, b


def is_contains(string, list_to_search):
    caunt_calls()
    for list_ in list_to_search:
        if string.lower() in list_.lower():
            return True
    return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'UrBan']))
print(is_contains('cyclid', ['recycling', 'cyclic']))
print(calls)


