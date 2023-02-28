"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""


def get_encoded_words(words):
    words_in_bytes = []

    for word in words:
        words_in_bytes.append(word.encode('utf-8'))
    
    return words_in_bytes


def get_decoded_words(words_in_bytes):
    words = []

    for word_in_byte in words_in_bytes:
        words.append(word_in_byte.decode('utf-8'))
    
    return words


words = ['разработка', 'администрирование', 'protocol']

encoded_words = get_encoded_words(words)

print(encoded_words)

decoded_words = get_decoded_words(encoded_words)

print(decoded_words)

