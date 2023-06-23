# Cadeias de Caracteres - Cadeias de texto - como manipular (famosa string)
#lembrar que string no Python é imutável

# frase = 'Curso em Video Python' (VARIÁVEL)


# FATIAMENTO DE STRING:

# frase[9]

# frase[9:13]

#OBS1: o python sempre exclui a última letra, ou seja, 9:13, vai do 9 até a letra(caracter) 12 - último valor não entra na contagem
#OBS2: é possível fatiar colocando uma unidade acima da máxima

# frase [9:21:2] - primeiro dois pontos é o range, segundo dois pontos determina a quantidade de espaços a serem pulados.

# frase [:5] - não começa em nada, ou seja, começa do primeiro caracter, até o cinco ou o último determninado

# frase [15:] - começa no 15 e não termina em nada, ou seja, termina no último caracter.

# frase [9::3] - primeiro dois pontos = linha 11 range, só com início, segundo dois pontos, número de pulos, no caso 3.


# ANÁLISE DE STRING:

# len(frase) - comprimento da frase.

# frase.count('o') - quantas vezes aparece o 'o'
# frase.count('o', 0, 13) - contagem com fatiamento, quantos 'o' existem no range 0:13 (lembrando que o 13 não é incluído).

# frase.find('deo') - quantas vezes encontrou 'deo'
# frase.find('android') - supondo que a frase que se usa o find esta escrito 'Curso em Vídeo Pyhton', o resultado da busca é -1
# 'Curso' in frase - há a palavra 'Curso' dentro da frase 'Curso em video Python' por exemplo. resultado: 'true'


# TRANSFORMAÇÃO

# MÉTODOS:

# frase.replace('Python', 'Android') - substitui a palavra 'Python' por 'Android'.

#frase.upper() - TUDO MAIÚSCULO

# frase.lower() - tudo minúsculo

# frase.capitalize() - Só a primeira letra em maiúsculo.

# frase.title() - analísa palavra por palavra, através dos espaços, assim deixa dos as letras iniciais maiúsculas, ex:
# 'Curso Em Video Python'.

# frase.strip() - remove todos os espaços do início e fim da frase.
# frase.rstrip() - remove somente os últimos espaços, ou seja, os à direita.
# frase.lstrip() - remove somente os primeiros espaços, ou seja, os à esquerda.


# DIVISÃO

# FUNCIONALIDADES:

# frase.split() - dividir as palavras numa lista única
# EX:
# normalmente fica assim:
# C u r s o   e m   v  í   d   e  o
# 0 1 2 3 4 5 6 7 8 9  10  11  12  13

# com split fica assim:

# C u r s o    e m   v í d e o
# 0 1 2 3 4    1 2   1 2 3 4 5

# '-'.join(frase) - juntar os nomes separados em listas
#OBS o separador '-' insere esse caracter entre os espaços das listas juntadas, tomando o exemplo acima, ficaria assim:
# 'Curso-em-Vídeo-Python'
#OBS2 se quiser espaços em branco, basta colocar ' '


#Prática:

'''frase = 'Curso em Vídeo Python'
print(frase)
print(frase[3])
print(frase[3:13])
print(frase[13:])
print(frase[:13])
print(frase[1:15:2])
print(frase[1::2])
print(frase[::2])

print("""Of Man’s First Disobedience, and the Fruit
Of that Forbidden Tree, whose mortal taste
Brought Death into the World, and all our woe""")
print(frase.count('o'))
print(frase.count('O'))
print(frase.upper())
print(frase.upper().count('O'))
print(len(frase))
print(frase.replace('Curso','Putaria'))
print('Curso' in frase)


# str é imutável, você não altera a variável.
# frase = 'Curso em Video Python'
# print (frase.replace('Python', 'Android')
# print(frase)
# output:Curso em Video Python

# para salver a mudança precisa refazer a variável:
# frase = frase.replace('Python', 'Android')'''

frase = 'Curso em Vídeo Python'
dividido = frase.split()
print(dividido[0])
print(dividido[2] [3])

# falta ver os exercícios



