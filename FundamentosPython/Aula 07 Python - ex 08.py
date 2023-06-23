#Faça um algortimo que leia o preço de um produto e mpostre seu novo preço com 5% de desconto
pr = float(input('Por favor digite o preço do seu produto: R$'))
off = pr - (pr * 5 / 100)
print (f'Seu produto com 5% de desconto sai por R${off:.2f}!')
