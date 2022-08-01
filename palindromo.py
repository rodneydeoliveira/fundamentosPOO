# Encontre o maior palíndromo, resultado do produto de 2 números com 4 dígitos.
# produto = multiplicação entre números
# encontrar um palíndromo (ex: 9889) multiplicando dois números com 4 dígitos

total = 0
lista = []
for i in range (10,100):
    for j in range (10,100):
        total = (i*j)
        total = str(total)
        lista.append(total)
print(lista)
palindromo = []
for numero in lista:
    inicio = 0
    fim = len(numero) - 1
    for i in range(len(numero) // 2):
        if numero[inicio] != numero[fim]:
            break
        inicio += 1
        fim -= 1
        palindromo.append(int(numero))

print(max(palindromo))
