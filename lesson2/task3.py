"""
Задание 3. Создать список и заполнить его элементами различных типов данных.
Реализовать проверку типа данных каждого элемента.
Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в
программе.
Пример:
для списка [5, "string", 0.15, True, None]
результат
<class 'int'>
<class 'str'>
<class 'float'>
<class 'bool'>
<class 'NoneType'>
"""

list_of_types = [5, "string", 0.15, True, None]
print(f"Для списка {list_of_types} рузультат:")
for value in list_of_types:
    print(type(value))


