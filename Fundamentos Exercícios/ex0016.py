# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira
# por exemplo: digite um número 6.127 tem a parte inteira 6.
# ver módulo math
'''from math import trunc
num = float(input('Digite um número real, como 12.4 2.345, etc:'))
print(f'O número digitado é {num}, sua parte inteira é {trunc(num)}')'''

num = float(input('Digite um número real, como 12.34, 45.893, etc:'))
print(f'O valor digitado é {num}, sua porção inteira é {int(num)}')

