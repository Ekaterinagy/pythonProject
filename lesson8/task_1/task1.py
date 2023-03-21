"""
1. Задание на закрепление знаний по модулю CSV. Написать скрипт,
осуществляющий выборку определенных данных из файлов info_1.txt, info_2.txt,
info_3.txt и формирующий новый «отчетный» файл в формате CSV.

Для этого:

Создать функцию get_data(), в которой в цикле осуществляется перебор файлов
с данными, их открытие и считывание данных. В этой функции из считанных данных
необходимо с помощью регулярных выражений извлечь значения параметров
«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
Значения каждого параметра поместить в соответствующий список. Должно
получиться четыре списка — например, os_prod_list, os_name_list,
os_code_list, os_type_list. В этой же функции создать главный список
для хранения данных отчета — например, main_data — и поместить в него
названия столбцов отчета в виде списка: «Изготовитель системы»,
«Название ОС», «Код продукта», «Тип системы». Значения для этих
столбцов также оформить в виде списка и поместить в файл main_data
(также для каждого файла);

Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл.
В этой функции реализовать получение данных через вызов функции get_data(),
а также сохранение подготовленных данных в соответствующий CSV-файл;

Пример того, что должно получиться:

Изготовитель системы,Название ОС,Код продукта,Тип системы

1,LENOVO,Windows 7,00971-OEM-1982661-00231,x64-based

2,ACER,Windows 10,00971-OEM-1982661-00231,x64-based

3,DELL,Windows 8.1,00971-OEM-1982661-00231,x86-based

Обязательно проверьте, что у вас получается примерно то же самое.

ПРОШУ ВАС НЕ УДАЛЯТЬ СЛУЖЕБНЫЕ ФАЙЛЫ TXT И ИТОГОВЫЙ ФАЙЛ CSV!!!
"""
import csv
import re


def write_to_csv(path_to_csv):
    main_data = get_data(['info_1.txt', 'info_2.txt', 'info_3.txt'])
    print(main_data)
    with open(path_to_csv, "w") as file:
        writer = csv.writer(file)
        writer.writerows(main_data)


def get_data(file_list):
    parse_parameters = (re.compile(r'Изготовитель системы:.*'),
                        re.compile(r'Название ОС:.*'),
                        re.compile(r'Код продукта:.*'),
                        re.compile(r'Тип системы:.*'))
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    print(file_list)
    main_data = [['Изготовитель системы', 'Название ОС', 'Код продукта',
                  'Тип системы']]
    for file_name in file_list:
        with open(file_name, "r", encoding="windows-1251") as file:
            text = file.read()
            os_prod_list.append(parse_parameters[0].findall(text)[0].split(':')
                                [1].lstrip())
            os_name_list.append(parse_parameters[1].findall(text)[0].split(':')
                                [1].lstrip())
            os_code_list.append(parse_parameters[2].findall(text)[0].split(':')
                                [1].lstrip())
            os_type_list.append(parse_parameters[3].findall(text)[0].split(':')
                                [1].lstrip())

    for key in range(len(file_list)):
        main_data.append([os_prod_list[key], os_name_list[key],
                          os_code_list[key], os_type_list[key]])
    return main_data


write_to_csv('my_data_report.csv')
