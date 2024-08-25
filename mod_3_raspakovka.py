def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)

print_params()
print_params(2,3)
print_params(b=25)
print_params(c = [1,2,3])

values_list = [1,'str', (1,2,3,4)]
values_dict = {'a': 23, 'b': 'dfr', 'c': ('jk','df')}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [7,'qwe']
print_params(*values_list_2,42)
