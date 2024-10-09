def count_string(file_name):
    file = open(file_name, 'r', encoding='utf-8')
    stringi = file.read()
    file.close()
    return stringi.count('\n')

def custom_write(file_name, strings):
    file = open(file_name, 'a', encoding='utf-8')
    strings_positions = {}
    stroka_zapisi = count_string(file_name) + 1
    for s in strings:
        strings_positions.update({(strings.index(s) + stroka_zapisi, file.tell()): s})
        file.write(s+'\n')
    file.close()
    return strings_positions

print(custom_write('111.txt', ['11111', '22222', '33333']))

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)