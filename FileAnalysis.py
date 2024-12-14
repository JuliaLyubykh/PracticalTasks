'''
Подготовка данных для записи в базу данных
'''
# Подключение файлов

# pip install gdown

import gdown

url = 'https://drive.google.com/drive/u/1/folders/1mczhXrDys25ylY3btR_d8_SN9RkpGwFN'
gdown.download_folder(url, quiet = False, remaining_ok = True)

# Чтение файлов

from glob import glob


all_files = glob('data/problem_*.md')
with open(filename, 'r') as f:
    data = f.read()

# Выделение из каждого файла формулировки и решения

import re

task_reg = re.compile('# Задача(.*)# Решение', re.MULTILINE | re.DOTALL)
sol_reg = re.compile('# Решение(.*)# Подсказки', re.MULTILINE | re.DOTALL)

# Сохранение в отдельный файл лог обработки

task = task_reg.findall(data)[0].strip()
solution = sol_reg.findall(data)[0].strip()

prob_id = int(filename.split('_')[1][:-3])

with open('log.txt', 'a') as f:
   f.write(f'Задача с ID {prob_id} обработана успешно!\n')

print('\n'.join(task.split('\n')[:5]))
