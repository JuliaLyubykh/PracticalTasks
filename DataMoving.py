'''
Написать программу, которая будет считывать содержимое файла, добавлять к
считанным строкам порядковый номер и сохранять их в таком виде в новом файле.
'''

# Имя исходного файла и имя целевого файла запрашивается у пользователя

# Каждая строка должна начинаться с ее номера, двоеточия и пробела, а после
# должен идти текст строки из исходного файла.

def add_line_numbers(file_name, new_file_name):
    with open(file_name, "r") as file:
        content = file.readlines()

        with open(new_file_name, "w") as new_file:
            for index, line in enumerate(content):
                new_file.write(f"{index+1}:{line}")

file_name = input("Введите имя исходного файла: ")
new_file_name = input("Введите имя целевого файла: ")

add_line_numbers(file_name, new_file_name)