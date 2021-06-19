def make_list(x):
    return x.split(',')


def make_lot(x):
    return set(x)


def make_dictionary(x, y):
    return dict(zip(x, y))


words = input('Введите через запятую список слов: ')
list_of_words = make_list(words)
print(list_of_words)
string_set = make_lot(list_of_words)
print(string_set)
number_of_elements = len(list_of_words)
print(f'В списке {number_of_elements} элемента')
symbols = input(f'Введите через запятую {number_of_elements} символов: ')
list_of_symbols = make_list(symbols)
my_dict = make_dictionary(list_of_words, list_of_symbols)
print(my_dict)

