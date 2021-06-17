import random
import math
while True:
    operation = input('Введите символ операции (+ - * / ** abs rand ! arccos): ')
    if operation == '+':
        operand1 = float(input('Введите первое слагаемое: '))
        operand2 = float(input('Введите второе слагаемое: '))
        result = float(operand1 + operand2)
        print(f'{operand1} {operation} {operand2} = {result}')
        yes_no = input('Чтобы продолжить нажмите "y"')
        if yes_no == 'y':
            continue
        else:
            break
    elif operation == '-':
        operand1 = float(input('Введите уменьшаемое: '))
        operand2 = float(input('Введите вычитаемое: '))
        result = float(operand1 - operand2)
        print(f'{operand1} {operation} {operand2} = {result}')
        yes_no = input('Чтобы продолжить нажмите "y"')
        if yes_no == 'y':
            continue
        else:
            break
    elif operation == '*':
        operand1 = float(input('Введите первый множитель: '))
        operand2 = float(input('Введите второй множитель: '))
        result = float(operand1 * operand2)
        print(f'{operand1} {operation} {operand2} = {result}')
        yes_no = input('Чтобы продолжить нажмите "y"')
        if yes_no == 'y':
            continue
        else:
            break
    elif operation == '/':
        operand1 = float(input('Введите делимое: '))
        operand2 = float(input('Введите делитель: '))
        result = float(operand1 / operand2)
        print(f'{operand1} {operation} {operand2} = {result}')
        yes_no = input('Чтобы продолжить нажмите "y"')
        if yes_no == 'y':
            continue
        else:
            break
    elif operation == '**':
        operand1 = float(input('Введите основание: '))
        operand2 = float(input('Введите степень: '))
        result = float(operand1 ** operand2)
        print(f'{operand1} {operation} {operand2} = {result}')
        yes_no = input('Чтобы продолжить нажмите "y"')
        if yes_no == 'y':
            continue
        else:
            break
    elif operation == 'abs':
        operand1 = float(input('Введите число: '))
        result = float(abs(operand1))
        print(f'Модуль числа {operand1} = {result}')
        yes_no = input('Чтобы продолжить нажмите "y"')
        if yes_no == 'y':
            continue
        else:
            break
    elif operation == 'rand':
        operand1 = float(input('Введите начало интервала: '))
        operand2 = float(input('Введите конец интервала: '))
        result = random.uniform(operand1, operand2)
        print(f'Случайное число = {result}')
        yes_no = input('Чтобы продолжить нажмите "y"')
        if yes_no == 'y':
            continue
        else:
            break
    elif operation == '!':
        operand1 = int(input('Введите число: '))
        result = math.factorial(operand1)
        print(f'Факториал числа {operand1} = {result}')
        yes_no = input('Чтобы продолжить нажмите "y"')
        if yes_no == 'y':
            continue
        else:
            break
    elif operation == 'arccos':
        operand1 = float(input('Введите число от -1 до 1: '))
        result = math.acos(operand1)
        print(f'Арккосинус числа {operand1} = {result}')
        yes_no = input('Чтобы продолжить нажмите "y"')
        if yes_no == 'y':
            continue
        else:
            break
