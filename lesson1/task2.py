"""
Задание 2.

Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
Пример:
Введите время в секундах: 3600
Время в формате ч:м:с - 1.0 : 60.0 : 3600

"""
print("Введите время в секундах: ")
n = int(input())
import time

time_format = time.strftime("%H:%M:%S", time.gmtime(n))
print("Время в формате ч:м:с ", time_format)