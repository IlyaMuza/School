my_dict = {'Vasya': 1975, 'Egor': 1999, 'Masha': 2002}
print(my_dict)
print(my_dict['Egor'])
print(my_dict.get('Semen'))
my_dict.update({'Svetlana': 2001, 'Fedya': 2002})
print(my_dict.pop('Egor'))
print(my_dict)

my_set = {1,2,'3',4.12,1,2,3,4}
print(my_set)
my_set.discard(1)
my_set.add((123,12,13))
my_set.add(123)
print(my_set)