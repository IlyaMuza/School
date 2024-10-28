import threading
from random import randrange
from time import sleep


class Bank:

    def __init__(self, balance=0):
        self.balance = balance
        self.lock = threading.Lock()

# по заданию пополнение работает всегда, когда поток вклинивается в программу
    def deposit(self):
        for i in range(100):
            print(f'{i+1} Пополнение поток заблокирован: {self.lock.locked()}')
            rand = randrange(50, 500)
            self.balance += rand
            print(f'{i+1} Пополнение: {rand}. Баланс: {self.balance}')
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            sleep(0.001)

# по заданию поток должен блокироваться до момента, пока на балансе не будет >500
    def take(self):
        for i in range(100):
            print(f'{i+1} Снятие поток заблокирован: {self.lock.locked()}')
            while self.lock.locked():  # костыль для срабатывания блокировки
                sleep(0.001)
            rand = randrange(50, 500)
            print(f'{i+1} Запрос на снятие {rand}')
            if rand > self.balance:
                print(f'{i + 1} Запрос отклонен, недостаточно средств. Сейчас поток снятия денег заблокирован: {self.lock.locked()}')
                self.lock.acquire()   # блокировка не работает
            else:
                self.balance -= rand
                print(f'{i+1} Снятие: {rand}. Баланс: {self.balance}')


bank1 = Bank()
thread10_3_1 = threading.Thread(target=Bank.deposit, args=(bank1,))
thread10_3_2 = threading.Thread(target=Bank.take, args=(bank1,))
thread10_3_1.start()
thread10_3_2.start()
thread10_3_2.join()
thread10_3_1.join()
print(f'Итоговый баланс: {bank1.balance}')
