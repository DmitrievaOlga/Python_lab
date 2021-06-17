text = input('Введите строку: ')
finish_text = ''
for i in range(0, len(text[:-1])):
    if i != 2:
        finish_text = finish_text + text[i]
print(finish_text)
print(f'Длина измененной строки {len(finish_text)} символов')
for i in text:
    if i == "c" or i == "с":
        print('В строке есть символ "с"')
