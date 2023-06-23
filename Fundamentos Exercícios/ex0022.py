# Crie um programa que leia o nome completo de uma pessoa e mostre:
# o nome com todas as letras maiúsculas
# o nome com todas as minúsculas
# Quantas letras ao todo (sem considerar os espaços)
# Quantas letras tem o primeiro nome
frase = str(input('Digite seu nome completo: ')).strip()
print('analisando seu nome:')
print(f'Em lestras maiúsuclas fica assim: {frase.upper()}')
print(f'Em lestras minúsculas fica assim: {frase.lower()}')
letras = len(frase) - frase.count(' ')
print(f'O total de letras de seu nome é {letras}')
#print(f'Seu primeiro nome tem {frase.find(" ")} letras')
div_nome = frase.split()
print(f'Seu primeiro nome possui {len(div_nome[0])} letras')
