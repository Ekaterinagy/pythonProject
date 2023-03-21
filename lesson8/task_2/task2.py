"""
2. Задание на закрепление знаний по модулю json. Есть файл orders
в формате JSON с информацией о заказах. Написать скрипт, автоматизирующий
его заполнение данными.

Для этого:
Создать функцию write_order_to_json(), в которую передается
5 параметров — товар (item), количество (quantity), цена (price),
покупатель (buyer), дата (date). Функция должна предусматривать запись
данных в виде словаря в файл orders.json. При записи данных указать
величину отступа в 4 пробельных символа;
Проверить работу программы через вызов функции write_order_to_json()
с передачей в нее значений каждого параметра.

ПРОШУ ВАС НЕ УДАЛЯТЬ ИСХОДНЫЙ JSON-ФАЙЛ
ПРИМЕР ТОГО, ЧТО ДОЛЖНО ПОЛУЧИТЬСЯ

{
    "orders": []
}

вам нужно подгрузить JSON-объект
и достучаться до списка, который и нужно пополнять
а потом сохранять все в файл
"""

import json
import os


def write_order_to_json(item, quantity, price, buyer, date):
    order = {"товар": item, "количество": quantity, "цена": price, "покупатель"
    : buyer, "дата": date}
    if os.stat("my_orders.json").st_size == 0:
        orders = {"orders": [order]}
    else:
        with open('my_orders.json', 'r', encoding='utf8') as json_file:
            orders = json.load(json_file)
            orders.get('orders').append(order)

    with open('my_orders.json', 'w', encoding='utf8') as json_file:
        json.dump(orders, json_file, indent=4, ensure_ascii=False)


write_order_to_json("принтер", 10, 100, "Ivanov I.I.", "24.09.2017")
write_order_to_json("принтер1", 11, 100, "Ivanov I.I.", "24.09.2017")
write_order_to_json("принтер2", 12, 100, "Ivanov I.I.", "24.09.2017")
write_order_to_json("принтер3", 13, 100, "Ivanov I.I.", "24.09.2017")
