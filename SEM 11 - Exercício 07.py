# 7. Escreva um programa que crie uma lista com os números de 1 a 100. Em seguida,
# imprima apenas os números pares da lista.

lista = []

for i in range (1,101):
    if i % 2 == 0:
        lista.append(i)
        print(i)

print(lista)
