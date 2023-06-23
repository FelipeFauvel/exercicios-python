# Crie um programa que leia quanto dinheiro ela tem na carteira e mostre quantos dólares ela pode comprar
var1 = float(input('Quanto você possui em sua carteira? R$'))
var2 = var1 // 4.92
var3 = var2%4.92
print (f'Levandro em conta, que a cotação do dólar hoje é 4,92, você pode comprar {var2:.0f} dólares e {var3:.2f} centávos de dólar')

