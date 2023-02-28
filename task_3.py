"""
Задание 3.

Определить, какие из слов «attribute», «класс», «функция», «type»
невозможно записать в байтовом типе с помощью маркировки b'' (без encode decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
--- обязательно!!! усложните задачу, "отловив" и обработав исключение,
придумайте как это сделать
"""

def convert_to_byte(words):
    for word in words:
        try:
            print(bytes(word, 'ascii'))
        except UnicodeEncodeError:
            print(f'Слово "{word}" невозможно энкодировать в байты через b')


words = ['attribute', 'класс', 'функция', 'type']

convert_to_byte(words)
