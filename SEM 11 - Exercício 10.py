# 10. Se você terminou os e[X]ercícios acima. Tente agora fazer o jogo da velha, mas
# utilizando listas.

# sinto q isso aqui é uma introducao pra matrizes rsrs
vitoriasJogador1 = 0
vitoriasJogador2 = 0
jogoAtivo = True
vitoria = False

tabuleiro = ["[1]","[2]","[3]", 
             "[4]","[5]","[6]",
             "[7]","[8]","[9]"]

posicaoOcupada = [0,0,0, # se a posicao foi ocupada, transforma o 0 em 1. isso é feito pra controlar se o jogador pode jogar ali ou nao
                  0,0,0,
                  0,0,0]
print()
print(tabuleiro[0],tabuleiro[1],tabuleiro[2])
print(tabuleiro[3],tabuleiro[4],tabuleiro[5])
print(tabuleiro[6],tabuleiro[7],tabuleiro[8])

while jogoAtivo:

    RodadaJogador1 = True

    while RodadaJogador1 and jogoAtivo:

        escolhaJogador1 = int(input("\nJogador 1, escolha a posição para jogar! (1 a 9)")) - 1

        if posicaoOcupada[escolhaJogador1] != 1 and escolhaJogador1 >= 0 and escolhaJogador1 <= 8: # checa se a posicao esta ocupada e a escolha esta no range do tabuleiro na verdade ta quebrado nao sei arrumar sem o try except

            posicaoOcupada[escolhaJogador1] = 1
            tabuleiro.pop(escolhaJogador1) # deleta na lista 
            tabuleiro.insert(escolhaJogador1, "[X]") # poe na lista a escolha do jogador
            
            print()
            print(tabuleiro[0],tabuleiro[1],tabuleiro[2])
            print(tabuleiro[3],tabuleiro[4],tabuleiro[5])
            print(tabuleiro[6],tabuleiro[7],tabuleiro[8])


            if tabuleiro[0] == "[X]" and tabuleiro[1] == "[X]" and tabuleiro[2] == "[X]": # horizontais
                print("\nJogador 1 ganhou!")
                jogoAtivo = False
                vitoria = True
            elif tabuleiro[3] == "[X]" and tabuleiro[4] == "[X]" and tabuleiro[5] == "[X]":
                print("\nJogador 1 ganhou!")
                jogoAtivo = False
                vitoria = True
            elif tabuleiro[6] == "[X]" and tabuleiro[7] == "[X]" and tabuleiro[8] == "[X]":
                print("\nJogador 1 ganhou!")
                jogoAtivo = False
                vitoria = True

            elif tabuleiro[0] == "[X]" and tabuleiro [3] == "[X]" and tabuleiro[6] == "[X]": # verticais
                print("\nJogador 1 ganhou!")
                jogoAtivo = False
                vitoria = True
            elif tabuleiro[1] == "[X]" and tabuleiro [4] == "[X]" and tabuleiro[7] == "[X]": 
                print("\nJogador 1 ganhou!")
                jogoAtivo = False
                vitoria = True
            elif tabuleiro[2] == "[X]" and tabuleiro [5] == "[X]" and tabuleiro[8] == "[X]": 
                print("\nJogador 1 ganhou!")
                jogoAtivo = False
                vitoria = True
            
            elif tabuleiro[0] == "[X]" and tabuleiro[4] == "[X]" and tabuleiro[8] == "[X]": # diagonais
                print("\nJogador 1 ganhou!")
                jogoAtivo = False
                vitoria = True
            elif tabuleiro[2] == "[X]" and tabuleiro[4] == "[X]" and tabuleiro[6] == "[X]": 
                print("\nJogador 1 ganhou!")
                jogoAtivo = False
                vitoria = True
            
        else:
            print("Escolha uma posição disponível!")
            continue
        
        RodadaJogador1 = False

    if posicaoOcupada == [1] * 9 and vitoria == False:
        print("\nDeu velha!")
        jogoAtivo = False

    RodadaJogador2 = True

    while RodadaJogador2 and jogoAtivo:

        escolhaJogador2 = int(input("\nJogador 2, escolha a posição para jogar! (1 a 9)")) - 1

        if posicaoOcupada[escolhaJogador2] != 1 and escolhaJogador2 >= 0 and escolhaJogador2 <= 8: # checa se a posicao esta ocupada e a escolha esta no range do tabuleiro

            posicaoOcupada[escolhaJogador2] = 1
            tabuleiro.pop(escolhaJogador2) # deleta na lista 
            tabuleiro.insert(escolhaJogador2, "[O]") # poe na lista a escolha do jogador

            print()
            print(tabuleiro[0],tabuleiro[1],tabuleiro[2])
            print(tabuleiro[3],tabuleiro[4],tabuleiro[5])
            print(tabuleiro[6],tabuleiro[7],tabuleiro[8])


            if tabuleiro[0] == "[O]" and tabuleiro[1] == "[O]" and tabuleiro[2] == "[O]": # horizontais
                print("\nJogador 2 ganhou!")
                jogoAtivo = False
                vitoria = True
            elif tabuleiro[3] == "[O]" and tabuleiro[4] == "[O]" and tabuleiro[5] == "[O]":
                print("\nJogador 2 ganhou!")
                jogoAtivo = False
                vitoria = True
            elif tabuleiro[6] == "[O]" and tabuleiro[7] == "[O]" and tabuleiro[8] == "[O]":
                print("\nJogador 2 ganhou!")
                jogoAtivo = False
                vitoria = True

            elif tabuleiro[0] == "[O]" and tabuleiro [3] == "[O]" and tabuleiro[6] == "[O]": # verticais
                print("\nJogador 2 ganhou!")
                jogoAtivo = False
                vitoria = True
            elif tabuleiro[1] == "[O]" and tabuleiro [4] == "[O]" and tabuleiro[7] == "[O]": 
                print("\nJogador 2 ganhou!")
                jogoAtivo = False
                vitoria = True
            elif tabuleiro[2] == "[O]" and tabuleiro [5] == "[O]" and tabuleiro[8] == "[O]": 
                print("\nJogador 2 ganhou!")
                jogoAtivo = False
                vitoria = True
            
            elif tabuleiro[0] == "[O]" and tabuleiro[4] == "[O]" and tabuleiro[8] == "[O]": # diagonais
                print("\nJogador 2 ganhou!")
                jogoAtivo = False
                vitoria = True
            elif tabuleiro[2] == "[O]" and tabuleiro[4] == "[O]" and tabuleiro[6] == "[O]": 
                print("\nJogador 2 ganhou!")
                jogoAtivo = False
                vitoria = True
            
        else:
            print("\nEscolha uma posição disponível!")
            continue
        
        RodadaJogador2 = False

# esse codigo esta extremamente repetitivo e com certeza tem um jeito melhor de fazer, mas vou deixar assim mesmo, foi legal 
