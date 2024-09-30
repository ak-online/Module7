def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding='utf-8')
    string_positions = {}
    num_start = 1
    byte_start = file.seek(0)
    for i in strings:
        file.write(i+'\n')
        key = (num_start, byte_start)
        string_positions[key]= i
        num_start += 1
        byte_start = file.tell()
    file.close()
    return string_positions

strings = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', strings)
for elem in result.items():
    print(elem)
