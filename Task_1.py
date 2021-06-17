number = int(input('Введите число '))
border_number = int(input('Введите пограничное число '))
if number < border_number:
    print('Ваше число меньше пограничного')
elif number > border_number:
    if number/border_number > 3:
        print('Ваше число больше пограничного более, чем в три раза')
    else:
        print('Ваше число больше пограничного')
else:
    print('Ваше число совпадает с пограничным')