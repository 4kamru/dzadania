# "Блокировки и обработка ошибок"
import time
import threading
from threading import Thread, Lock
from time import sleep
import random

class Bank(Thread):
    # balance - баланс банка(int), lock - объект класса Lock для блокировки потоков
    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    # 100 транзакций пополнения средств, разблокировка счета, если баланс >= 500
    def deposit(self):
        i = 0
        while i < 100:
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()

            # как бы пополнение счета на случайную сумму от 50 до 500
            popolnenie = random.randint(50, 500)
            self.balance += popolnenie
            print(f'Пополнение: {popolnenie}. Баланс: {self.balance}\n')
            # задержка - имитация скорости выполнения пополнения счета
            sleep(0.001)
            i += 1
    def take(self):
        i = 0
        while i < 100:
            snyatie = random.randint(50, 500)
            print(f'Запрос на {snyatie}')
            if snyatie <= self.balance:
                self.balance -= snyatie
                print(f'Снятие: {snyatie}. Баланс: {self.balance}\n')
            else:
                print(f'Запрос отклонён, недостаточно средств\n')
                self.lock.acquire()
            # задержка - имитация скорости выполнения пополнения счета
            sleep(0.001)
            i += 1


bk = Bank()
# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))
th1.start()
th2.start()
th1.join()
th2.join()
print(f'Итоговый баланс: {bk.balance}')



