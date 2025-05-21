# 1. Escreva um programa que crie uma lista com números aleatórios e a imprima na
# tela.

import random
lista = []

for i in range(random.randint(0,100)):
    lista.append(random.randint(0,100)) 

print(lista)