'''
Написать программу, которая будет удалять все комментарии из исходного файла
с кодом на языке Python.
Сохранить содержимое в созданном файле.
'''

# Обрабатывать ошибки

# Имена файла назначения и файла источника запрашиваются у пользователя

def remove(file_name, new_file_name):
    try:
        with open(file_name, "r") as file:
            content = file.readlines()
            stripped_content = []
            for line in content:
                stripped_line = line.split('#')[0].strip()
                stripped_content.append(stripped_line)
        with open(new_file_name, "w") as new_file:
            new_file.write('\n'.join(stripped_content))
    except:
        print('Не удалось открыть входной файл')
    
file_name = input('Введите имя исходного файла: ')
new_file_name = input('Введите имя файла для вывода: ')
remove(file_name, new_file_name)
