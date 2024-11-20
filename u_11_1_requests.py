import requests

r = requests.get('https://api.github.com/events', stream=True, timeout=5)
print(r)
print(r.url)    # проверить URL-адрес
print(r.text[:100]) # прочитать содержимое ответа сервера
print(r.cookies)    # Если ответ содержит некоторые файлы cookie, вы можете быстро получить к ним доступ
print(r.encoding)   # позволяет узнать, какую кодировку использует Requests, при необходимости - сменить
print(r.content[:100])  # получить доступ к телу ответа в виде байтов для нетекстовых запросов
print('JSON:')
for i in range(3):
    print(r.json()[i])  # ответ в формате JSON

filename = 'test_requests.txt'
with open(filename, 'wb') as fd:    # сохранение ответа в файл
    for ch in r.iter_content(chunk_size=128):
        fd.write(ch)
print('\nЗаголовки:')
for i, v in r.headers.items():
    print(i, ':' , v)

url = 'https://api.github.com/some/endpoint'
headers = {'Server': 'github.com'}
r = requests.get(url, headers=headers)  # добавить HTTP-заголовки к запросу
print(r.text)
