#Faça um valor que leia um ângulo qualquer e mostre o valor do seu senom, cosseno e tangente desse ângulo
# eixo vertical seno, eixo horizontal cosseno, projeção de um ângulo específico, usar módulo.

from math import radians, sin, cos, tan
num = float(input('Digite um ângulo qualquer: '))
print (f' O seno deste número é {sin(radians(num)):.3f}')
print (f'O cosseno deste número é {cos(radians(num)):.3f}')
print (f'A tangente deste número é {tan(radians(num)):.3f}')

'''from math import radians
num = float(input('Digite um número: '))
print (f'O radiano deste número é {radians(num)}')'''
