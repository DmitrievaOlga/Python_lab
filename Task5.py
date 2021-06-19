words = input('Введите через запятую список слов: ')
list_of_words = words.split(',')
print(list_of_words)
lot_of_words = set(list_of_words)
print(lot_of_words)
number_of_elements = len(list_of_words)
print(f'В списке {number_of_elements} элемента')
symbols = input(f'Введите через запятую {number_of_elements} символов: ')
list_of_symbols = symbols.split(',')
my_dict = dict(zip(list_of_words, list_of_symbols))
print(my_dict)





