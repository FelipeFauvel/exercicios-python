#Faça um algrotimo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.
nome = input('Digite seu nome para comerçarmos!')
print (input(f'Olá,{nome}! Por favor, tecle "enter" para continuarmos!'))
pr = float(input(f'{nome}, por favor diga seu salário total, sem descontos: R$'))
reajuste = pr + (pr * 15 / 100)
print(f'{nome}, seu salário reajustado, com aumento de 15%, fica {reajuste:.2f}')
