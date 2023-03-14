"""
Задание 6. В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
Решите через рекурсию. В задании нельзя применять циклы.
"""
import random


def random_number(num, attempt_count=1):
    n = int(input("Введите число: "))
    if attempt_count == 10:
        print(f"Вы не угадали число :-(. Загаданное число: {num}")
        return

    attempt_count += 1
    if n == num:
        print("Ура, вы угадали число!!!")
        return
    elif n < num:
        print("Ваше число меньше загаданного")
    elif n > 100:
        print("Введите число в диапозоне от 0 до 100")
    elif n > num:
        print("Ваше число больше загаданного")
    random_number(num, attempt_count)


num = random.randint(1, 100)
random_number(num)
