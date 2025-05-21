# 5. Escreva um programa que crie uma lista de palavras e imprima a palavra mais
# longa e a palavra mais curta da lista.

lista = ["arroz", "feijao", "banana", "palavramuitogrande", "ola", "professora", "tudo", "bom", "vc", "é", "legal"]
menor = float('inf')
maior = float('-inf')

for palavra in lista:

    if len(palavra) < menor:
        menor = len(palavra)
        menorPalavra = palavra

    if len(palavra) > maior:
        maior = len(palavra)
        maiorPalavra = palavra

print(lista)
print(f"Maior palavra: {maiorPalavra}")
print(f"Menor palavra: {menorPalavra}")