import threading
import time
from queue import Queue
from random import randrange
from threading import Thread


class Table:

    def __init__(self, number, guest=None):
        self.number = number
        self.guest = guest

class Guest(Thread):

    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        rand = randrange(3,10)
        time.sleep(rand)

class Cafe:

    def __init__(self, *tables):
        self.queue = Queue()
        self.tables = tables

    def guest_arrival(self, *guests):
        for guest in guests:
            for table in self.tables:
                if not table.guest:
                    table.guest = guest
                    guest.start()
                    print(f'{guest.name} сел(-а) за стол номер {table.number}')
                    break
            if not guest.is_alive():
                self.queue.put(guest)
                print(f'{guest.name} в очереди')

    def discuss_guest(self):
        while not self.queue.empty() or (any (table.guest for table in self.tables)):
            for table in self.tables:
                if table.guest and not table.guest.is_alive():
                    print(f'{table.guest.name} покушал и ушел', f'Стол {table.number} свободен')
                    table.guest = None
                if not self.queue.empty() and not table.guest:
                    table.guest = self.queue.get()
                    print(f'{table.guest.name} вышел из очереди и сел за стол номер {table.number}')
                    table.guest.start()


tables = [Table(number) for number in range (1, 6)]
guest_names = ['Marina','Oleg','Vaghtang','Sergey','Darya','Arman','Victoria','Nikita','Galina','Pavel','Ilya','Alex']
guests = [Guest(name) for name in guest_names]
cafe = Cafe(*tables)
cafe.guest_arrival(*guests)
cafe.discuss_guest()










# Материал лекции
'''
def getter(queue):
    while True:
        try:
            time.sleep(3)
            item = queue.get(timeout=2)
            print(item)
        except Exception:
            break

q = Queue()
thread1 = threading.Thread(target=getter, args=(q,), daemon=False)
thread1.start()

for i in range(10):
    time.sleep(2)
    q.put(i)
    print(threading.current_thread(), 'положил', i)

#q.put(5)
#print(q.get(timeout=2))
#print('End program')
'''