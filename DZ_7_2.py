def custom_write(file_name, strings):
    strings_positions = {}

    with open(file_name, 'w', encoding='UTF-8') as file:
        for line_number, string in enumerate(strings, start=1):
            byte_position = file.tell()
            encoded_string = string.encode('utf-8')
            print(f"String {line_number} length in bytes: {len(encoded_string) + 1}")  # +1 для символа новой строки
            file.write(string + '\n')
            strings_positions[(line_number, byte_position)] = string

    return strings_positions

#Пример использования функции
if __name__ == '__main__':
    info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
    ]

    result = custom_write('text.txt', info)
    for elem in result.items():
        print(elem)