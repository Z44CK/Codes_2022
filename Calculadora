#Primeiro projeto de calculadora simples e fácil

import math

while True:
    num1 = input('Informe o numero: ')
    operador = input('Operador: ')
    num2 = input('Informe o numero: ')

    if not num1.isnumeric() or not num2.isnumeric():
        print('Valor incorreto, o valor precisa ser um numero!')
        continue
    num1 = int(num1)
    num2 = int(num2)

    if operador == '+':
        print(num1 + num2)
        break
    elif operador == '-':
        print(num1 - num2)
        break
    elif operador == '*':
        print(num1 * num2)
        break
    elif operador == '/':
        print(f'{num1 / num2:.2f}')
        break
    elif operador == '++': # Lembrando que o simbolo de '+' duas vezes, não eleva um numero, eu apenas o criei para facilitar o input no teclado
        print(f'O valor de {num1:.2f} elevado a {num2:.2f} é: {math.pow(num1, num2):.2f}')
        break
    else:
        print('Operador invalido!')
