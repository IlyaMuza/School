def add_everything_up(a, b):
    a, b = bool_int_float_reverse(a), bool_int_float_reverse(b)
    try:
        if type(a) == bool and type(b) == bool:
            return a or b
        return a + b
    except TypeError:
        return str(a) + str(b)

def bool_int_float_reverse(a):
    if a == 'True':
        a = True
    elif a == 'False':
        a = False
    else:
        try:
            a = int(a)
        except:
            try:
                a = float(a)
            except:
                a = str(a)
    return a

print(add_everything_up(1,2))
print(add_everything_up('asd','qwer'))
print(add_everything_up(12,'sfgsd'))
a = 'True'
b = 'False'
print(add_everything_up(a, b))
a = input()
b = input()
print(add_everything_up(a, b))