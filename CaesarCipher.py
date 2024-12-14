'''
Написать программу, которая реализует код Цезаря дял латинского алфавита.
Пользователь должен иметь возможность ввода последовательности символов (фразы).
'''
# Идея шифрования заключается в циклическом сдвиге букв на три позиции.
# Пример: буква A становится D, B - в E, и т.д. 
# Последние три буквы переносятся на начало.

def cipher_caesar(text):
    result = ""
    for char in text:
        if char.isalpha():
            shift_char = ord(char) + 3
            if char.isupper():
                if shift_char <= ord ("Z"):
                    result += chr(shift_char) 
                else:
                    chr(shift_char - 26)
            else:
                if shift_char <= ord("z"):
                    result += chr(shift_char)
                else:
                    chr(shift_char - 26)
        else:
            result += char
    return result

print("Зашифрованный текст: ", cipher_caesar(input("Введите фразу: ")))
