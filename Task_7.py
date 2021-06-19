import random
import math


class Calc:

    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def subtract(x, y):
        return x - y

    @staticmethod
    def multiply(x, y):
        return x * y

    @staticmethod
    def divide(x, y):
        return x / y

    @staticmethod
    def power(x, y):
        return x ** y

    @staticmethod
    def mod(x):
        return abs(x)

    @staticmethod
    def rand(x, y):
        return random.uniform(x, y)

    @staticmethod
    def fact(x):
        return math.factorial(x)

    @staticmethod
    def arccos(x):
        return math.acos(x)


while True:
    operation = input('Введите символ операции (+ - * / ** abs rand ! arccos): ')
    if operation == '+':
        operand1 = float(input('Введите первое слагаемое: '))
        operand2 = float(input('Введите второе слагаемое: '))
        result = Calc.add(operand1, operand2)
        print(f'{operand1} {operation} {operand2} = {result}')
        yes_no = input('Чтобы продолжить нажмите "y"')
        if yes_no == 'y':
            continue
        else:
            break
    elif operation == '-':
        operand1 = float(input('Введите уменьшаемое: '))
        operand2 = float(input('Введите вычитаемое: '))
        result = Calc.subtract(operand1, operand2)
        print(f'{operand1} {operation} {operand2} = {result}')
        yes_no = input('Чтобы продолжить нажмите "y"')
        if yes_no == 'y':
            continue
        else:
            break
    elif operation == '*':
        operand1 = float(input('Введите первый множитель: '))
        operand2 = float(input('Введите второй множитель: '))
        result = Calc.multiply(operand1, operand2)
        print(f'{operand1} {operation} {operand2} = {result}')
        yes_no = input('Чтобы продолжить нажмите "y"')
        if yes_no == 'y':
            continue
        else:
            break
    elif operation == '/':
        operand1 = float(input('Введите делимое: '))
        operand2 = float(input('Введите делитель: '))
        result = Calc.divide(operand1, operand2)
        print(f'{operand1} {operation} {operand2} = {result}')
        yes_no = input('Чтобы продолжить нажмите "y"')
        if yes_no == 'y':
            continue
        else:
            break
    elif operation == '**':
        operand1 = float(input('Введите основание: '))
        operand2 = float(input('Введите степень: '))
        result = Calc.power(operand1, operand2)
        print(f'{operand1} {operation} {operand2} = {result}')
        yes_no = input('Чтобы продолжить нажмите "y"')
        if yes_no == 'y':
            continue
        else:
            break
    elif operation == 'abs':
        operand1 = float(input('Введите число: '))
        result = Calc.mod(operand1)
        print(f'Модуль числа {operand1} = {result}')
        yes_no = input('Чтобы продолжить нажмите "y"')
        if yes_no == 'y':
            continue
        else:
            break
    elif operation == 'rand':
        operand1 = float(input('Введите начало интервала: '))
        operand2 = float(input('Введите конец интервала: '))
        result = Calc.rand(operand1, operand2)
        print(f'Случайное число = {result}')
        yes_no = input('Чтобы продолжить нажмите "y"')
        if yes_no == 'y':
            continue
        else:
            break
    elif operation == '!':
        operand1 = int(input('Введите целое неотрицательное число: '))
        result = Calc.fact(operand1)
        print(f'Факториал числа {operand1} = {result}')
        yes_no = input('Чтобы продолжить нажмите "y"')
        if yes_no == 'y':
            continue
        else:
            break
    elif operation == 'arccos':
        operand1 = float(input('Введите число от -1 до 1: '))
        result = Calc.arccos(operand1)
        print(f'Арккосинус числа {operand1} = {result}')
        yes_no = input('Чтобы продолжить нажмите "y"')
        if yes_no == 'y':
            continue
        else:
            break
