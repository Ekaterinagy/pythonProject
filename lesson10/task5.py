"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""

import subprocess

import chardet


def _ping(ARGS):
    result = subprocess.Popen(ARGS, stdout=subprocess.PIPE)

    for line in result.stdout:
        ch = chardet.detect(line)
        print(line.decode(encoding=ch.get("encoding")))


args1 = ['ping', 'yandex.ru', '-c', '4']
args2 = ['ping', 'youtube.com', '-c', '4']
_ping(args1)
_ping(args2)
