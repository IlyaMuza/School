from pprint import pprint

def apply_all_func(int_list: list, *functions):
    results = dict()
    for function in functions:
        try:
            results.update({function.__name__: function(int_list)})
        except TypeError:
            print('Неверный тип введенных данных')
    return results


pprint(apply_all_func([6,3,-7,8,12.1,0,34,2,-1,14,6.5,54,121], max, min, len, sum, sorted,
                      reversed, all, any, chr))
print(type(apply_all_func))