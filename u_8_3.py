class IncorrectVinNumber(Exception):
    message = None
    name = 'Ошибка VIN номера'

    def __init__(self, message):
        self.message = message


class IncorrectCarNumbers(Exception):
    message = None
    name = 'Ошибка номера машины'

    def __init__(self, message):
        self.message = message


class Car:

    def __init__(self, model, vin, number):
        if not self.__is_valid_vin(vin):
            raise IncorrectVinNumber(IncorrectVinNumbers.message)
        if not self.__is_valid_numbers(number):
            raise IncorrectCarNumbers(IncorrectCarNumbers.message)
        self.__vin = vin
        self.__numbers = number
        self.model = model

    def get_vin(self):
        return self.__vin

    def set_vin(self, vin):
        if not self.__is_valid_vin(vin):
            raise IncorrectVinNumber(IncorrectVinNumbers.message)
        self.__vin = vin

    def get_number(self):
        return self.__numbers

    def set_number(self, number):
        if not self.__is_valid_numbers(number):
            raise IncorrectCarNumbers(IncorrectCarNumbers.message)
        self.__numbers = number

    def __is_valid_vin(self, vin_number):
        key = False
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber('Некорректный ввод VIN-номера автомобиля, проверьте тип данных')
        elif not 1000000 <= vin_number <=9999999:
            raise IncorrectVinNumber('Неверный диапазон для VIN-номера автомобиля')
        else:
            key = True
        return key

    def __is_valid_numbers(self, numbers):
        key = False
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        elif len(numbers) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')
        else:
            key = True
        return key


try:
    car1 = Car('First', 1234567, 'v567bn')
except IncorrectVinNumber as IVN:
    print(IVN.message)
except IncorrectCarNumbers as ICN:
    print(ICN.message)
else:
    print(f'{car1.model} успешно создан')

try:
    car2 = Car('Секонд', 123456789, 'v567bn')
except IncorrectVinNumber as IVN:
    print(IVN.message)
except IncorrectCarNumbers as ICN:
    print(ICN.message)
else:
    print(f'{car2.model} успешно создан')

try:
    car3 = Car('Ферд', 1234567, 'Считать не удалось')
except IncorrectVinNumber as IVN:
    print(IVN.message)
except IncorrectCarNumbers as ICN:
    print(ICN.message)
else:
    print(f'{car3.model} успешно создан')

try:
    car4 = Car('Жигули 4-ка', 1234567, 3.1427)
except IncorrectVinNumber as IVN:
    print(IVN.message)
except IncorrectCarNumbers as ICN:
    print(ICN.message)
else:
    print(f'{car4.model} успешно создан')

try:
    car5 = Car('Жигули 5-ка', 'А123Я', 'РВУДНО')
except Exception as exc:
    print(exc.name, exc.message)
else:
    print(f'{car5.model} успешно создан')

print(car1.model, car1.get_vin(), car1.get_number())

try:
    car1.set_vin(112233445566)
except Exception as exc:
    print(exc.message)
else:
    print(f'VIN номер машины {car1.model} успешно сменен')

try:
    car1.set_number(112233445566)
except Exception as exc:
    print(exc.message)
else:
    print(f'Номер машины {car1.model} успешно сменен')