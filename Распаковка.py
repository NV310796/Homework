def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(b = 25)
print_params(c = [1,2,3])

values_list = [2, 'string', False]
values_dict = {'a':'123', 'b':4, 'c':2.1}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = ['one', 2.0]

print_params(*values_list_2, 42)