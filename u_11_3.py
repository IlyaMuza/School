import sys
from pprint import pprint
import inspect

class MyClass:
    attr_list = []
    attr_dict = {}
    attr_int = 42
    func_add = lambda x: x + 1

    def __init__(self, *args):
        for i in args:
            self.value = [self.func_add for x in range(i)]

    def func1_MyClass(self):
        return True

    def func2_MyClass(self, a):
        print(a)

def introspection_info(obj):
    result = {}
    result['type'] = type(obj)
    list_method_2 = [m[0] for m in inspect.getmembers(obj, predicate=inspect.ismethod)]
    list_method = [m[0] for m in inspect.getmembers(obj, predicate=callable)]
    list_attr = [a for a in dir(obj) if a not in list_method]

    result['attributes'] = list_attr
    result['methods'] = list_method
    result['module'] = inspect.getmodule(obj)
#    result['call_not_in_ismethod'] = [a for a in list_method if a not in list_method_2]
    return result

primer = MyClass(5)

res = introspection_info(primer)
for i, v in res.items():
    print(i, v)