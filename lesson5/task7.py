"""
Задание 7. Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.
Пример:
для n = 5
1+2+3+4+5 = 5(5+1)/2
Нужно написать рекурсивную ф-цию только для левой части выражения!
Результат нужно сверить с правой частью.
Правой части выражения в рекурсивной ф-ции быть не должно!
Решите через рекурсию. В задании нельзя применять циклы.
"""


def sum_elements(сounter, result=0, result_str=""):
    if сounter < 1:
        result_list.append(result_str[::-1])
        result_list.append(result)
        return

    else:
        result_str = result_str + str(сounter)
        if сounter - 1 != 0:
            result_str += "+"

        result += сounter

        сounter -= 1
        return sum_elements(сounter, result, result_str)
        print(f'{result}')


n = int(input("Введите число: "))
m = n * (n + 1) / 2

print(f"для n = {n}")
result_list = []
sum_elements(n)
print(f"сумма: :{result_list[0]}={n}*({n}+1)/2")
if m == result_list[1]:
    print("равны")
else:
    print("неравны")
