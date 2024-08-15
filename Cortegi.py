immutable_var = 1, 2, 'asd', [1,2,12,'fgh']
print(immutable_var)
mutable_list = [1,2,'1','2']
mutable_list.append(12)
mutable_list.extend([13,[1,2]])
mutable_list[3] = 3
print(mutable_list)
mutable_list.pop(1)
print(mutable_list)
mutable_list.remove(1)
print(mutable_list)

