"""
Задание 2.

Каждое из слов «class», «function», «method» записать в байтовом формате
без преобразования в последовательность кодов
не используя!!! методы encode и decode)
и определить тип, содержимое и длину соответствующих переменных.

Подсказки:
--- b'class' - используйте маркировку b''
--- используйте списки и циклы, не дублируйте функции
"""

def render_words_info(words):
    for word in words:
        print(f"Тип - {type(word)} Содержимое - {word}, Длина - {len(word)}")


byte_words = [b'class', b'function', b'method']

render_words_info(byte_words)
