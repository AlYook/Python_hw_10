"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""


import subprocess
import chardet


def ping_host(host):
    args = ['ping', host]

    ping_command = subprocess.Popen(args, stdout=subprocess.PIPE)

    for line in ping_command.stdout:
        encoding_info = chardet.detect(line)

        print(line.decode(encoding_info['encoding']))


ping_host('yandex.ru')
ping_host('youtube.com')
