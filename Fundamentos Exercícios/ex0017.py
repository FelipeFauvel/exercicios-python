#Faça um programa que leia o cumprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa
# quadrado da hipotenusa é igual o quadrado dos catetos, ou usar a biblioteca de matemática.
import math
cat1 = float(input('Digite um número que será o cateto oposto: '))
cat2 = float(input('Digite um número que será o cateto adjacente: '))
print (f'usando por base as dimenões de catetos {cat1}X{cat2}, seu triângulo retângulo possui a hipotenusa de {math.sqrt(cat1 * cat1 + cat2 * cat2):.2f}')
# pode colocar a função hypot math.hypot (cat1, cat2)
# pode usar a forma matemática pura, criando mais uma variável:

# cat1 = float(input('Digite um número inteiro que será o cateto 1: '))
# cat2 = float(input('Digite um número inteiro que será o cateto 2: '))
# hypot = (cat ** 2 + cat2 ** 2) ** (1/2)
