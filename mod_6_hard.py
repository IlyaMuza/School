from math import pi


class Figure:
    sides_count = 0
    filled = True
    __sides = None

    def __is_valid_color(self, r, g, b):
        return 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255

    def __init__(self, color, *sides):
        if isinstance(color, tuple) and self.__is_valid_color(*color):
            self.__color = color
        else:
            self.__color = (0, 0, 0)
        self.__sides = []
        if self.__is_valid_sides(*sides):
            for s in sides:
                self.__sides.append(s)
        else:
            for _ in range(self.sides_count):
                self.__sides.append(1)

    def get_color(self):
        return self.__color

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)
        else:
            print(f'Цвет некорректный, оставляем старый {self.__color}')

    def __is_valid_sides(self, *args):
        if len(args) != self.sides_count:
            return False
        for x in args:
            if x <= 0:
                return False
        else:
            return True

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if len(new_sides) != self.sides_count:
            print(f'Вы ввели {'мало' if len(new_sides) < self.sides_count else 'много'} сторон')
            return
        for i in range(self.sides_count):
            self.__sides[i] = new_sides[i]


class Circle(Figure):
    sides_count = 1
    __radius = 0.0

    def __init__(self, color, sides):
        super().__init__(color,  sides)
        if isinstance(sides, int | float):
            self.__radius = float(sides) / (2 * pi)

    def get_square(self):
        return pi * self.__radius ** 2


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    def get_square(self):
        return ((p := len(self) / 2) * (p - self.get_sides()[0]) * (p - self.get_sides()[1]) *
                (p - self.get_sides()[2])) ** 0.5


class Cube(Figure):
    sides_count = 12
    __sides = [1] * 12

    def __init__(self, color, sides):
        if isinstance(sides, int | float):
            self.__sides = [sides] * 12
        super().__init__(color, *self.__sides)

    def get_volume(self):
        return self.get_sides()[0] ** 3


figure = Figure((255, 255, 255), 10, 20, 20)
print(figure._Figure__sides, figure._Figure__color)
print(figure.get_color())
print(*figure.get_sides())
print(len(figure))
figure.set_sides(40, 30, 30)
print(*figure.get_sides())
print('-'*50)

triangle = Triangle((2, 2, 2), 20)
print(triangle.get_sides())
triangle.set_sides(40, 40, 40, 40)
print(triangle.get_sides())
triangle.set_sides(40, 40, 40)
print(triangle.get_sides())
print(len(triangle))
print(triangle.get_square())
print('-'*50)

circle1 = Circle((1, 1, 1), 7)
print(circle1._Circle__radius)
print(circle1.get_square())
print(circle1.get_color())
print(circle1.get_sides())
circle1.set_sides(10, 11, 12)
circle1.set_sides(12)
print(circle1.get_sides())
circle1.set_color(255, 366, 899)
circle1.set_color(255, 0, -255)
circle1.set_color(255, 125, 100)
print(circle1.get_color())
print('-'*50)

cube = Cube((4, 4, 4), 5)
print(cube.get_sides())
print(cube.get_volume())
print('-'*50)

circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
