"""
1. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите два варианта решения: через list и через dict.

Пример:
Введите номер месяца: 10
Результат через список: Осень
Результат через словарь: Осень
"""

winter = "Winter"
spring = "Spring"
summer = "Summer"
autumn = "Autumn"

season_list = [winter, winter, spring, spring, spring, summer, summer,
               summer, autumn, autumn, autumn, winter]
season_dict = {1: winter, 2: winter, 3: spring, 4: spring, 5: spring,
               6: summer, 7: summer, 8: summer, 9: autumn, 10: autumn,
               11: autumn, 12: winter}
n = int(input("Введите номер месяца: "))
if 13 > n > 0:
    print(f"Результат через список: {season_list[n - 1]}")
    print(f"Результат через словарь: {season_dict[n]}")
else:
    print("Такого месяца нет")


