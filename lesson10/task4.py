"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""

res = ['разработка', 'администрирование', 'protocol', 'standard']
for n in res:
    n_bytes = n.encode('utf-8')
    print(f'{n_bytes},{type(n_bytes)}')
    n_str = n_bytes.decode('utf-8')
    print(f'{n_str},{type(n_str)}')
