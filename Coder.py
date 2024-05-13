# ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz
# АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдежзийклмнопрстуфхцчшщъыьэюя
# _alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдежзийклмнопрстуфхцчшщъыьэюя"
#
# matrxix = [[] for i in _alphabet]
# print(matrxix)
#
# phrase = 'кто я'
# phrase = ''.join(e for e in phrase if e.isalnum())
# key = 'хз'
#
# count = 0
#
# code = ''
# _start = ord(_alphabet[0])
# print(_alphabet)
#
# for i in range(len(phrase)):
#     key_letter_code = ord(key[i % len(key)]) - _start
#     phrase_letter_code = ord(phrase[i]) - _start
#
#     print(f"{key_letter_code} {phrase_letter_code}")
#     code += chr(_start + ((key_letter_code + phrase_letter_code) % len(_alphabet)))
import random

import pandas as pd
class Alphabet:
    alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    start = ord(alphabet[0])

class Coder:

    def __init__(self):
        self.replace_map = {'ё': 'e', ' ': ''}
        self.preprocessing = [str.lower]

    def encode(self, phrase: str, key: str):
        phrase = self._preprocessing(phrase)
        key = self._preprocessing(key)
        return self._encode(phrase, key)

    def decode(self, phrase: str, key: str):
        phrase = self._preprocessing(phrase)
        key = self._preprocessing(key)
        return self._decode(phrase, key)


    # region text validation
    def _replace(self, text: str) -> str:
        for key in self.replace_map.keys():
            text = text.replace(key, self.replace_map[key])
        return text

    def _preprocessing(self, text: str) -> str:
        # Заменяем символы по предустановленным правилам
        text = self._replace(text)

        # Приводим букавки в нижний регистр
        text = text.lower()

        # Оставляем только циферки и букавки
        text = ''.join(e for e in text if e.isalnum())

        return text

    # endregion

    # region encode decode algorithms
    def _encode(self, phrase: str, key: str) -> str:
        encoded = ''

        for i in range(len(phrase)):
            key_letter_code = ord(key[i % len(key)]) - Alphabet.start
            phrase_letter_code = ord(phrase[i]) - Alphabet.start

            #print(f"{key_letter_code} {phrase_letter_code}")
            encoded += chr(Alphabet.start + ((key_letter_code + phrase_letter_code) % len(Alphabet.alphabet)))
        return encoded

    def _decode(self, encoded: str, key: str) -> str:
        decoded = ''

        for i in range(len(encoded)):
            key_letter_code = ord(key[i % len(key)]) - Alphabet.start
            phrase_letter_code = ord(encoded[i]) - Alphabet.start

            #print(f"{key_letter_code} {phrase_letter_code}")
            decoded += chr(Alphabet.start + ((phrase_letter_code - key_letter_code) % len(Alphabet.alphabet)))
        return decoded
    # endregion

import random
def generate_key() -> str:
    length = random.randint(10, 30)
    key = ''
    for i in range(length):
        key += Alphabet.alphabet[random.randint(0, len(Alphabet.alphabet) - 1)]
    return key

if __name__ == "__main__":
    print(generate_key())

