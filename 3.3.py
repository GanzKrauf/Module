def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params()
print_params(b = 25)
print_params(c = [1, 2, 3])
values_list = [1, 'Kok', [1, 2]]
value_dict = {'a': 2, 'b': 'line', 'c': False}
print_params(*values_list)
print_params(**value_dict)
value_list2 = [54.32, 'Строка']
print_params(*value_list2, 42)
