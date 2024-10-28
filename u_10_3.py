import threading
from random import randrange
from time import sleep


class Bank:

    def __init__(self, balance=0):
        self.balance = balance
        self.lock = threading.Lock()


    def deposit(self):
        for i in range(100):
            print(f'{i+1} Пополнение поток заблокирован: {self.lock.locked()}')
            while not self.lock.locked():
                sleep(0.001)
            rand = randrange(50, 500)
            self.balance += rand
            print(f'{i+1} Пополнение: {rand}. Баланс: {self.balance}')
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            sleep(0.001)
        for i in range(100):
            if self.lock.locked():
                self.lock.release()
            sleep(0.001)


    def take(self):
        for i in range(100):
            print(f'{i+1} Снятие поток заблокирован: {self.lock.locked()}')
            while self.lock.locked():
                sleep(0.001)
            rand = randrange(50, 500)
            print(f'{i+1} Запрос на снятие {rand}')
            while rand > self.balance:
                print(f'{i + 1} Запрос отклонен, недостаточно средств. Сейчас поток снятия денег заблокирован: {self.lock.locked()}')
                self.lock.acquire()
                self.lock.acquire()
                print(f'{i + 1} Запрос на снятие {rand}')
            self.balance -= rand
            print(f'{i+1} Снятие: {rand}. Баланс: {self.balance}')

        for i in range(100):
            self.lock.acquire()
            sleep(0.001)


bank1 = Bank()
thread10_3_1 = threading.Thread(target=Bank.deposit, args=(bank1,))
thread10_3_2 = threading.Thread(target=Bank.take, args=(bank1,))
thread10_3_1.start()
thread10_3_2.start()
for i in range(200):
    sleep(0.01)
if bank1.lock.locked():
    bank1.lock.release()
thread10_3_1._stop()
thread10_3_2._stop()
print(f'Итоговый баланс: {bank1.balance}')
