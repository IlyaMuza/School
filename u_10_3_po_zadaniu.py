import threading
import time
from random import randrange
from time import sleep

class Bank:

    def __init__(self, balance=0):
        self.balance = balance
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            rand = randrange(50, 500)
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            self.balance += rand
            print(f'+{i+1} Пополнение: {rand}. Баланс: {self.balance}')
            sleep(0.01)

    def take(self):
        for i in range(100):
            rand = randrange(50, 500)
            print(f'-{i+1} Запрос на снятие {rand}')
            if rand > self.balance:
                print(f'-{i + 1} Запрос отклонен, недостаточно средств. Сейчас поток снятия денег заблокирован: {self.lock.locked()}')
                sleep(0.01)
                self.lock.acquire()
            else:
                self.balance -= rand
                print(f'-{i+1} Снятие: {rand}. Баланс: {self.balance}')
                sleep(0.01)


bank1 = Bank()
thread10_3_1 = threading.Thread(target=Bank.deposit, args=(bank1,))
thread10_3_2 = threading.Thread(target=Bank.take, args=(bank1,))
thread10_3_1.start()
thread10_3_2.start()
thread10_3_1.join()
thread10_3_2.join()
print(f'Итоговый баланс: {bank1.balance}')
