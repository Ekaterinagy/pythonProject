"""
Задача 32: Определить индексы элементов массива (списка),
значения которых принадлежат заданному диапазону (т.е. не меньше заданного
минимума и не больше заданного максимума)
"""
import random


def generate_random_list(size=20, left=-10, right=90):
    r_list = []
    for _ in range(size):
        r_list.append(random.randint(left, right))
    return r_list


def find_indexes(r_list, min_border, max_border):
    index_dict = []

    for i in range(len(r_list)):

        if min_border <= r_list[i] <= max_border:
            index_dict.append(i)

    return index_dict


random_list = generate_random_list()
print(f"Заданный случайный массив {random_list}")
min_border = int(input("Введите первую границу: "))
max_border = int(input("Введите вторую границу: "))

if min_border > max_border:
    t = min_border
    min_border = max_border
    max_border = t

print(f"Найденные индексы: {find_indexes(random_list, min_border, max_border)}"
      )
