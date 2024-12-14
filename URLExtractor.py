'''
Создать функцию для извлечения URL
'''

import re

def extract_url_without_scheme(web_url):
    # Регулярное выражение для поиска схемы доступа
    scheme_pattern = r'^([a-z]+://)'
    
    # Найти схему доступа в URL
    match = re.search(scheme_pattern, web_url)
    
    # Если схема найдена, удалить её из URL
    if match:
        trimmed_url = web_url[len(match.group(0)):]
    else:
        trimmed_url = web_url
    
    return trimmed_url

print(extract_url_without_scheme(input('Введите URL: ')))  
