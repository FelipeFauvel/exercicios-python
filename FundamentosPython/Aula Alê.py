def calcular_delta(valor_a, valor_b, valor_c):
    print('dentro da função')
    return valor_b ** 2 - 4 * valor_a * valor_c

print('fora da função')


a = 1
b = 5
c = -14
x1 = (-b + calcular_delta(a, b, c) ** (1 / 2)) / (2 * a)
x2 = (-b - calcular_delta(a, b, c) ** (1 / 2)) / (2 * a)
print(f'x1 = {x1}\nx2 = {x2}')
# teste git commit
