'''
Написать программу для выведения на экран объединенного содержимого нескольких
файлов. В процессе работы программа должна выдавать сообщения о том, какие
файлы открыть не удается, и переходить к следующим.
'''

# Имена файлов передаются в качестве аргументов
# Файлы объединяются в том порядке, в котором указаны
# Если программа была запущена без аргументов, вывести сообщение об ошибке

def combined_files(*file_names):
    if len(file_names) == 0:
        print("Ошибка: файлы не указаны.")
    else:
        combined_content = ""
        for file_name in file_names:
            try:
                with open(file_name, "r") as file:
                    combined_content += file.read() + '\n'
            except:
                print(f"Файл {file_name} не открывается.")
        print(combined_content)

combined_files(input("Введите название первого файла: "), input("Введите название второго файла: "))
