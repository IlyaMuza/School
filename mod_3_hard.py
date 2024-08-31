def str_or_int(elem):
    if type(elem) == int:
        return elem
    if type(elem) == str:
        return len(elem)

def calculate_structure_sum(*args):
    if len(args) == 0:
        return 0
    elem = args[0]
    if (type(elem) == int or type(elem) == str):
        if len(args) != 1:
            return str_or_int(elem) + calculate_structure_sum(*args[1:])
        else:
            return str_or_int(elem)
    if type(elem) == tuple or type(elem) == list or type(elem)==set:
        if len(args) != 1:
            return calculate_structure_sum(*elem) + calculate_structure_sum(*args[1:])
        else:
            return calculate_structure_sum(*elem)
    if type(elem) == dict:
        if len(args) != 1:
            return calculate_structure_sum(*(elem.items())) + calculate_structure_sum(*args[1:])
        else:
            return calculate_structure_sum(*(elem.items()))


data_srtucture = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

print(calculate_structure_sum(*data_srtucture))






#

#

#print(result)