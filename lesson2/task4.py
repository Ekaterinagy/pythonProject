"""
Задание 4. Для списка реализовать обмен значений соседних элементов,
т.е. значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
Пример:
Введите целые числа через пробел: 1 2 3 4
Результат: 2 1 4 3
Введите целые числа через пробел: 1 2 3
Результат: 2 1 3
"""

list_1 = []
for element in input("Введите целые числа через пробел: ").split():
    list_1.append(int(element))
if len(list_1)%2 ==0:
    list_1[::2], list_1[1::2] = list_1[1::2], list_1[::2]
else:
    list_1[:len(list_1)-1:2], list_1[1:len(list_1)-1:2] = \
    list_1[1:len(list_1)-1:2], list_1[:len(list_1)-1:2]
print(f"Результат: {list_1}")



