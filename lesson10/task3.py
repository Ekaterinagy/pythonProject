"""
Задание 3.

Определить, какие из слов «attribute», «класс», «функция», «type»
невозможно записать в байтовом типе с помощью маркировки b'' (
без encode decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
--- обязательно!!! усложните задачу, "отловив" исключение,
придумайте как это сделать
"""
import ast

words = ['attribute', 'класс', 'функция', 'type']

print('1 способ')
words_with_error = []
for word in words:
    encode_needed = False
    for char in word:
        if not char.isascii():
            encode_needed = True
            break
    if encode_needed:
        words_with_error.append(word)
print(words_with_error)
print('2 способ')
for word in words:
    try:
        result = ast.literal_eval("b'" + word + "'")
        print(result, type(result))
    except:
        print(f'слово "{word}" нельзя представить в виде b''')
