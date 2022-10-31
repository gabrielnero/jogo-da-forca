import os
from util import configura_jogo, gerar_palavra_secreta, exibir_jogo, exibir_jogo_sem_dica, mostrar_dica, comparar_chute, op_invalida, salva_partida, exibe_historico, jogar_novamente

jogar = True
while jogar:
    nomes = True
    while nomes:
        jogador = input("Insira o nome do jogador: ")
        desafiante = input("Insira o nome do desafiante: ")
        if len(jogador) >= 2 and len(desafiante) >= 2:
            nomes = False
        else: 
            os.system("cls")
            print("Os nomes devem possuir mais de 2 caracteres!")


    os.system("cls")
    
    palavra_chave_dicas = configura_jogo(desafiante)
    palavra_chave = palavra_chave_dicas[0]

    dica_1 = palavra_chave_dicas[1]
    dica_2 = palavra_chave_dicas[2]
    dica_3 = palavra_chave_dicas[3]

    rodada = True
    
    os.system("cls")

    vencedor = ""
    palavra_censurada = gerar_palavra_secreta(palavra_chave)

    dicas = [dica_1, dica_2, dica_3]
    contador_dicas = 0
    
    erros = 0
    
    while (rodada):
        if contador_dicas < 3:
            exibir_jogo(palavra_chave, dica_1, dica_2, dica_3, palavra_censurada, erros)
            op = input("Insira uma opção: ")        
        else:
            exibir_jogo_sem_dica(palavra_chave, palavra_censurada, erros)
            op = "2"
        
        if op == "1":
            contador_dicas = mostrar_dica(dicas, contador_dicas)
            chute = input("Chute uma letra: ")
            comparacao = comparar_chute(chute, palavra_chave, palavra_censurada, erros)
            palavra_censurada = comparacao[0]
            erros = comparacao[1]
            
        elif op == "2":
            chute = input("Chute uma letra: ")
            comparacao = comparar_chute(chute, palavra_chave, palavra_censurada, erros)
            palavra_censurada = comparacao[0]
            erros = comparacao[1]
            
        else:   
            op_invalida()
            continue

        if erros == 5:
            rodada = False
            print("O Desafiante {} venceu!" .format(desafiante))
            vencedor = "Desafiante"
            
            print("    _______________         ")
            print("   /               \       ")
            print("  /                 \      ")
            print("//                   \/\  ")
            print("\|   XXXX     XXXX   | /   ")
            print(" |   XXXX     XXXX   |/     ")
            print(" |   XXX       XXX   |      ")
            print(" |                   |      ")
            print(" \__      XXX      __/     ")
            print("   |\     XXX     /|       ")
            print("   | |           | |        ")
            print("   | I I I I I I I |        ")
            print("   |  I I I I I I  |        ")
            print("   \_             _/       ")
            print("     \_         _/         ")
            print("       \_______/           ")

        elif palavra_censurada == palavra_chave.upper():
            rodada = False
            print("O jogador {} venceu!" .format(jogador))
            def imprime_mensagem_vencedor():
                print("Parabéns, você ganhou!")
        print("       ___________      ")
        print("      '._==_==_=_.'     ")
        print("      .-\\:      /-.    ")
        print("     | (|:.     |) |    ")
        print("      '-|:.     |-'     ")
        print("        \\::.    /      ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       ")
        vencedor = "Jogador"

    salva_partida(desafiante, jogador, palavra_chave, vencedor)
    exibe_historico()
    jogar = jogar_novamente()