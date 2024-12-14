'''
Создать функцию для поиска дат в тексте
'''

# Формат: YYYY-MM-DD, где YYYY - год, MM - месяц и DD - день
# Вернуть список найденных в тексте дат

import re

def find_dates_in_text(text):
    r = r'[0-9]{4} -(?:0[1-9]|1[0-2])-(?:0[1-9]|[12][0-9]|3[01])'
    return re.findall(re.compile(r, re.X), text)
