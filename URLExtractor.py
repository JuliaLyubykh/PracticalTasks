'''
Создать функцию для извлечения URL
'''

import re

def extract_url_without_scheme(web_url):
    scheme_pattern = r'^([a-z]+://)'
    match = re.search(scheme_pattern, web_url)
    if match:
        trimmed_url = web_url[len(match.group(0)):]
    else:
        trimmed_url = web_url
    return trimmed_url

print(extract_url_without_scheme(input('Введите URL: ')))  
