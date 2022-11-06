# Importar ferramentas
import os
from util import configura_jogo, gerar_palavra_secreta, exibir_jogo, exibir_jogo_sem_dica, mostrar_dica, comparar_chute, \
    op_invalida, salva_partida, exibe_historico, jogar_novamente

# Setup de variáveis
jogar = True
while jogar:
    nomes = True
    while nomes:
        nome_jogador = input("Insira o nome do jogador: ").capitalize()
        nome_desafiante = input("Insira o nome do desafiante: ").capitalize()
        if len(nome_jogador) < 2 or len(nome_desafiante) < 2:
            os.system("cls")
            print("Os nomes devem possuir mais de 2 caracteres!")
        else:
            nomes = False

    os.system("cls")

# Configurações do jogo

    palavra_chave_dicas = configura_jogo(nome_desafiante)
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
            exibir_jogo(palavra_chave, palavra_censurada, erros)
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
            print("O Desafiante {} venceu!".format(nome_desafiante))
            vencedor = "Desafiante"
            print('''
                _______________         
               /               \       
              /                 \      
            //                   \/\  
            \|   XXXX     XXXX   | /  
             |   XXXX     XXXX   |/     
             |   XXX       XXX   |      
             |                   |      
             \__      XXX      __/     
               |\     XXX     /|       
               | |           | |        
               | I I I I I I I |        
               |  I I I I I I  |        
               \_             _/       
                 \_         _/         
                   \_______/           
            ''')

        elif palavra_censurada == palavra_chave.upper():
            rodada = False
            print("O jogador {} venceu!".format(nome_jogador))
            print('''        
               ___________      
              '._==_==_=_.'     
              .-\\:      /-.    
             | (|:.     |) |    
              '-|:.     |-'     
                \\::.    /      
                 '::. .'        
                   ) (          
                 _.' '._        
                '-------'       
                 ''')
            vencedor = "Jogador"

# Histórico de partidas / finalização
    salva_partida(vencedor, nome_desafiante, nome_jogador, palavra_chave)
    exibe_historico()
    jogar = jogar_novamente()
