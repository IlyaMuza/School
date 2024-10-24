from pyexpat.errors import messages


class StepValueError(ValueError):

    def __init__(self, message):
        self.message = message

class Iterator:

    def __init__(self, *args):
        if len(args) == 0:
            raise StepValueError('Итератору не заданы исходные данные')
        if len(args) == 1:
            self.start = 0
            self.stop = args[0]
            self.step = 1
        if len(args) == 2:
            self.start = args[0]
            self.stop = args[1]
            self.step = 1
        if len(args) == 3:
            self.start = args[0]
            self.stop = args[1]
            self.step = args[2]
        if not self.__is_true_data():
            raise StepValueError(messages)
        self.pointer = self.start


    def __iter__(self):
        self.pointer = self.start
        return self


    def __next__(self):
        while (self.pointer <= self.stop and self.step > 0) or (self.pointer >= self.stop and self.step < 0):
            self.pointer += self.step
            return self.pointer - self.step
        raise StepValueError('Итератор закончил работу')


    def __is_true_data(self):
        if self.step == 0:
            raise StepValueError('Неверно указан шаг итератора')
        if (self.start < self.stop and self.step < 0) or (self.start > self.stop and self.step > 0):
            raise StepValueError('Исходные данные заданы некорректно')
        return True


try:
    iter1 = Iterator(100,200,0)
    for i in iter1:
        print(i, end=' ')
except StepValueError as SVE:
    print(SVE.message)

try:
    iter2 = Iterator(50)
    for i in iter2:
        print(i, end=' ')
except StepValueError as SVE:
    print(SVE.message)

try:
    iter3 = Iterator(1,6)
    for i in iter3:
        print(i, end=' ')
except StepValueError as SVE:
    print(SVE.message)

try:
    iter4 = Iterator(10,1,-2)
    for i in iter4:
        print(i, end=' ')
except StepValueError as SVE:
    print(SVE.message)

try:
    iter5 = Iterator(5,2,3)
    for i in iter5:
        print(i, end=' ')
except StepValueError as SVE:
    print(SVE.message)

try:
    iter6 = Iterator()
    for i in iter6:
        print(i, end=' ')
except StepValueError as SVE:
    print(SVE.message)