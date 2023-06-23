nome = input('Digite seu nome:')
n1 = float(input('Qual a sua nota do 1º bimestre prova?: '))
n2 = float(input('Qual a sua nota do 2º bimestre prova?: '))
n3 = float(input('Qual a sua nota do 3º bimestre prova?: '))
n4 = float(input('Qual a sua nota do 4º bimestre prova?: '))
m = (n1 + n2 + n3 + n4) / 4
print(f'{nome}, sua média final é {m:.2f}')
print(m > 7)
if m >= 7:
    print('Você foi aprovado com sucesso! Parabéns! Continue sendo um aluno exemplar! :)')
if m < 7:
    print('Você foi reprovado, tente se esforçar mais da próxima vez :(')






