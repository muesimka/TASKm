import os
import time
from multiprocessing import Process

def task1():
    print(f"Процесс 1 запущен. ID: {os.getpid()}")
    time.sleep(2)
    print("Функция 1 завершена")

def task2():
    print(f"Процесс 2 запущен. ID: {os.getpid()}")
    time.sleep(3)
    print("Функция 2 завершена")

def task3():
    print(f"Процесс 3 запущен. ID: {os.getpid()}")
    time.sleep(1)
    print("Функция 3 завершена")

def task4():
    print(f"Процесс 4 запущен. ID: {os.getpid()}")
    time.sleep(4)
    print("Функция 4 завершена")


if __name__ == "__main__":

    p1 = Process(target=task1)
    p2 = Process(target=task2)
    p3 = Process(target=task3)
    p4 = Process(target=task4)

    p1.start()
    print(f"Запущен процесс p1, ID: {p1.pid}")

    p2.start()
    print(f"Запущен процесс p2, ID: {p2.pid}")

    p3.start()
    print(f"Запущен процесс p3, ID: {p3.pid}")

    p4.start()
    print(f"Запущен процесс p4, ID: {p4.pid}")

    p1.join()
    p2.join()
    p3.join()
    p4.join()

    print("Все процессы завершили работу.")