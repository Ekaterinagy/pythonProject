"""
Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
повторениями).
Выдать без повторений в порядке возрастания все те числа, которые встречаются
в обоих наборах.
Пользователь вводит 2 числа.
n - кол-во элементов первого множества.
m - кол-во элементов второго множества.
Затем пользователь вводит сами элементы множеств.
"""
def get_user_input_number_list(size, message):
    numbers_list = []
    for value in input(message).split():
        numbers_list.append(int(value))

    if len(numbers_list) != size:
        raise Exception("Количество элементов не соответствует входному "
                        "размеру!")
    return numbers_list


n = int(input("кол-во элементов первого множества: "))
m = int(input("кол-во элементов второго множества: "))
n_list = get_user_input_number_list(n, "Введите значение для n списка через "
                                       "пробел: ")
m_list = get_user_input_number_list(m, "Введите значение для m списка через "
                                       "пробел: ")
res_list = list(set.intersection(set(n_list), set(m_list)))
res_list.sort()
print(res_list)