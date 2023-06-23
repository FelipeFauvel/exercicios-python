#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade necessária para pintá-lo, sabendo que a cada litro de tinta pinta uma área de 2m²
a = float(input('Digite a largura de uma parede:'))
l = float(input('Digite a altura desta parede:'))
ar = a * l
tinta = ar / 2
print (f'Sua parde tem a dimensão de {a}x{l}, sendo assim a área dessa parede mede {ar:.2f}m²')
print (f'Portanto, para pintar esta parede, você precisará de {tinta:.1f} litros de tinta, visto que cada litro cobre cerca de 2m² da parede')



