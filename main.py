
#ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz
#АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдежзийклмнопрстуфхцчшщъыьэюя
matrxix = [[] for i in alphabet]
print(matrxix)

phrase = 'who am i'
phrase = ''.join(e for e in phrase if e.isalnum())
key = 'xd'

count = 0

code = ''
start = ord(alphabet[0])
print(alphabet)

for i in range(len(phrase)):

    key_letter_code = ord(key[i % len(key)]) - start
    phrase_letter_code = ord(phrase[i]) - start

    print(f"{key_letter_code} {phrase_letter_code}")
    code += chr(start + ( (key_letter_code + phrase_letter_code) % len(alphabet) ) )

print(code)
decode = ''

for i in range(len(code)):

    key_letter_code = ord(key[i % len(key)]) - start
    phrase_letter_code = ord(code[i]) - start

    print(f"{key_letter_code} {phrase_letter_code}")
    decode += chr(start + ( ( phrase_letter_code - key_letter_code) % len(alphabet) ) )

print(decode)