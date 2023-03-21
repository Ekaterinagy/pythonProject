"""
3. Задание на закрепление знаний по модулю yaml.
 Написать скрипт, автоматизирующий сохранение данных
 в файле YAML-формата.
Для этого:

Подготовить данные для записи в виде словаря, в котором
первому ключу соответствует список, второму — целое число,
третьему — вложенный словарь, где значение каждого ключа —
это целое число с юникод-символом, отсутствующим в кодировке
ASCII(например, €);

Реализовать сохранение данных в файл формата YAML — например,
в файл file.yaml. При этом обеспечить стилизацию файла с помощью
параметра default_flow_style, а также установить возможность работы
с юникодом: allow_unicode = True;

Реализовать считывание данных из созданного файла и проверить,
совпадают ли они с исходными.
"""
import yaml

data = {'items': ['computer', 'printer', 'keyboard', 'mouse'],
        'items_ptice': {'computer': '200€-1000€', 'keyboard': '5€-50€', 'mouse'
        : '4€-7€', 'printer': '100€-300€'},
        'items_quantity': 4}

with open('my_file.yaml', 'w', encoding='utf8') as f:
    yaml.dump(data, f, encoding='utf8', default_flow_style=True, allow_unicode=
    True)

with open('my_file.yaml', 'r', encoding='utf8') as f:
    my_file = yaml.safe_load(f)
    print(my_file)
print(f"my_file equals data = {data == my_file}")

'''
output
{'items': ['computer', 'printer', 'keyboard', 'mouse'], 'items_ptice': 
{'computer': '200€-1000€', 'keyboard': '5€-50€', 'mouse': '4€-7€', 'printer': 
'100€-300€'}, 'items_quantity': 4}
my_file equals data = True
'''
