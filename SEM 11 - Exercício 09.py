# 9. Escreva um programa que crie uma lista com as letras do alfabeto e embaralhe
# suas posições. Em seguida, peça ao usuário para adivinhar a posição correta de
# uma determinada letra e informe se ele acertou ou errou.
import random

alfabeto = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

random.shuffle(alfabeto)

letraEscolhida = input("Digite uma letra para adivinhar a posição: ") 

posicaoLetra = alfabeto.index(letraEscolhida.lower())

posicaoEscolhida = int(input("Digite uma posição entre 1 e 26!")) - 1

print(f"{alfabeto}")

if posicaoEscolhida == posicaoLetra:
    print("Parabéns!! Você acertou!!!")
else:
    print("Não foi dessa vez amigo!")



