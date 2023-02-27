"""
Задача 2: Найдите сумму цифр трехзначного числа.
*Пример:*

123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0) |

"""

num = int(input("Введите трехзначное число: "))
n1 = num % 10
temp = int(num / 10)
a = num % 10
n2 = temp % 10
temp = int(temp / 10)
n3 = temp % 10
result = n1 + n2 + n3
print(num, " ->", result, f"({n3}+{n2}+{n1})")
