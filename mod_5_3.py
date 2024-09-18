class House:

    def __init__(self, name, number_of_floors):
        self.name = str(name)
        self.number_of_floors = int(number_of_floors)

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print(f'В доме \'{self.name}\' этажа {new_floor} не существует')
        else:
            for i in range(1, new_floor+1):
                print(f'Дом \'{self.name}\' этаж {i}')

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __eq__(self,other):
        if not isinstance(other, (int, House)):
            raise TypeError("Операнд справа должен иметь тип int или House")
        elif isinstance(other,int):
            return self.number_of_floors == other
        else:
            return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        if not isinstance(other, (int, House)):
            raise TypeError("Операнд справа должен иметь тип int или House")
        elif isinstance(other,int):
            return self.number_of_floors < other
        else:
            return self.number_of_floors < other.number_of_floors

    def __le__(self,other):
        if not isinstance(other, (int, House)):
            raise TypeError("Операнд справа должен иметь тип int или House")
        elif isinstance(other,int):
            return self.number_of_floors <= other
        else:
            return self.number_of_floors <= other.number_of_floors

    def __gt__(self,other):
        if not isinstance(other, (int, House)):
            raise TypeError("Операнд справа должен иметь тип int или House")
        elif isinstance(other,int):
            return self.number_of_floors > other
        else:
            return self.number_of_floors > other.number_of_floors

    def __ge__(self,other):
        if not isinstance(other, (int, House)):
            raise TypeError("Операнд справа должен иметь тип int или House")
        elif isinstance(other,int):
            return self.number_of_floors >= other
        else:
            return self.number_of_floors >= other.number_of_floors

    def __ne__(self,other):
        if not isinstance(other, (int, House)):
            raise TypeError("Операнд справа должен иметь тип int или House")
        elif isinstance(other,int):
            return self.number_of_floors != other
        else:
            return self.number_of_floors != other.number_of_floors

    def __add__(self, other):
        if not isinstance(other, (int, House)):
            raise TypeError("Операнд справа должен иметь тип int или House")
        elif isinstance(other, int):
            self.number_of_floors += other
            return self
        else:
            self.number_of_floors += other.number_of_floors
            self.name += f' вместе с домом {other.name}'
            return self

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        return self + other

    def __sub__(self, other):
        if not isinstance(other, (int, House)):
            raise TypeError("Операнд справа должен иметь тип int или House")
        elif isinstance(other, int):
            self.number_of_floors -= other
            return self
        else:
            self.number_of_floors -= other.number_of_floors
            self.name += f' без дома {other.name}'
            return self

    def __rsub__(self, other):
        if not isinstance(other, (int, House)):
            raise TypeError("Операнд справа должен иметь тип int или House")
        elif isinstance(other, int):
            self.number_of_floors = other - self.number_of_floors
            return self
        else:
            self.number_of_floors -= other.number_of_floors
            self.name += f' без дома {other.name}'
            return self

    def __mul__(self, other):
        if not isinstance(other, (int, House)):
            raise TypeError("Операнд справа должен иметь тип int или House")
        elif isinstance(other, int):
            self.number_of_floors = self.number_of_floors * other
            return self
        else:
            self.number_of_floors = self.number_of_floors * other.number_of_floors
            self.name += f' умноженный на дом {other.name}'
            return self

    def __rmul__(self, other):
        return self * other

    def __imul__(self, other):
        return self * other

    def __truediv__(self, other):
        if not isinstance(other, (int, House)):
            raise TypeError("Операнд справа должен иметь тип int или House")
        elif isinstance(other, int):
            self.number_of_floors = self.number_of_floors / other
            return self
        else:
            self.number_of_floors = self.number_of_floors / other.number_of_floors
            self.name += f' поделенный на дом {other.name}'
            return self

    def __rtruediv__(self, other):
        if isinstance(other, int):
            self.number_of_floors = other / self.number_of_floors
            return self
        else:
            raise TypeError("Операнд справа должен иметь тип int или House")

    def __floordiv__(self, other):
        if not isinstance(other, (int, House)):
            raise TypeError("Операнд справа должен иметь тип int или House")
        elif isinstance(other, int):
            self.number_of_floors = self.number_of_floors // other
            return self
        else:
            self.number_of_floors = self.number_of_floors // other.number_of_floors
            self.name += f' нацелоподеленный на дом {other.name}'
            return self

    def __rfloordiv__(self, other):
        if isinstance(other, int):
            self.number_of_floors = other // self.number_of_floors
            return self
        else:
            raise TypeError("Операнд справа должен иметь тип int или House")

    def __mod__(self, other):
        if not isinstance(other, (int, House)):
            raise TypeError("Операнд справа должен иметь тип int или House")
        elif isinstance(other, int):
            self.number_of_floors = self.number_of_floors % other
            return self
        else:
            self.number_of_floors = self.number_of_floors % other.number_of_floors
            self.name += f' осталось после деления на дом {other.name}'
            return self

    def __rmod__(self, other):
        if isinstance(other, int):
            self.number_of_floors = other % self.number_of_floors
            return self
        else:
            raise TypeError("Операнд справа должен иметь тип int или House")


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)

h3 = House('ЖК Мамулино', 17)
h4 = House('Калининский', 10)
h5 = House('Домик в городе', 18)
h3.go_to(7)
h4.go_to(12)
h3.go_to(-2)

print(h1==16, h1==h5, h1==18, h1==h2)
print(h1<h2, h1>h2, h1<=h2, h1>=h2, h1<20, h1>20)
print(h1<=18, h1<=20, h1>=18, h1>=20, h1!=h2, h1!=h5)
print(h1!=18, h1!=20)
print(len(h1),len(h2), len(h3))
print(str(h4))
print(str(h3))
print(h1, h2, sep='   @@@   ')
print(h1 + 2)
print(2 + h1)
h1 += 2
print(h1)
print(h1+h3)
print(h1-3)
print(50-h1)
print(h1-h2)
print(h2 * 2)
print(h2 * h2)
print(h2 / 2)
print(h2 / h1)
print(h3 // 2)
print(2 // h4)
print((h5 + 1) % 2)
print(5 % (h5+2))
print(h5 % h3)