# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido
# usar módulo randomico.

from random import choice
n1 = input('digite o primeiro nome: ')
n2 = input('digite o segundo nome: ')
n3 = input('digite o terceiro nome: ')
n4 = input('digite o terceiro nome: ')
lista = [n1, n2, n3, n4]
print(f'O resultado de seu sorteio é {choice(lista)}')