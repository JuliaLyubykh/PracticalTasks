'''
Создать функцию для поиска дат в тексте
'''

# Формат: YYYY-MM-DD, где YYYY - год, MM - месяц и DD - день
# Вернуть список найденных в тексте дат

import re

def find_dates_in_text(text):
    r = r"""
            # Ищем начало слова, в том числе YYYY-MM-DD
            \b

            # Варианты YYYY от 0000 до 9999
            [0-9]{4}

            # Разделитель
            -

            # Варианты MM от 01 до 12: 01-09, 10-12
            (?:0[1-9]|1[0-2])

            # Разделитель
            -

            # Варианты DD от 01 до 31: 01-09, 10-19, 20-29, 30-31
            (?:0[1-9]|[12][0-9]|3[01])

            # Ищем конец слова, в том числе YYYY-MM-DD
            \b
        """

    return re.findall(re.compile(r, re.X), text)