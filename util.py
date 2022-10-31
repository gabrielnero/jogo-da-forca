import os
import time

def configura_jogo(desafiante):
    try:
        palavra_chave = input(desafiante + " insira a palavra chave: ")
        dica_1 = input(desafiante + " insira a dica número 1: ")
        dica_2 = input(desafiante + " insira a dica número 2: ")
        dica_3 = input(desafiante + " insira a dica número 3: ")

        retorno = [palavra_chave, dica_1, dica_2, dica_3]
    except:
        print("Insira valores válidos!")
    return retorno


def gerar_palavra_secreta(palavra_chave):
    palavra_secreta = ""
    numero_caracteres = len(palavra_chave)

    for index in range(0, numero_caracteres):
        palavra_secreta += "*"
    return palavra_secreta


def exibir_jogo(palavra_chave, dica_1, dica_2, dica_3, palavra_secreta, erros):
    dicas = [dica_1, dica_2, dica_3]
    contador = 0
    os.system("cls")
    print("A palavra chave possuí {} letras." .format(len(palavra_chave)))
    exibe_palavra_erros(palavra_secreta, erros)
    print("[1] Receber dica")
    print("[2] Adivinhar letra")


def exibir_jogo_sem_dica(palavra_chave, palavra_secreta, erros):
    os.system("cls")
    print("A palavra chave possuí {} letras." .format(len(palavra_chave)))
    exibe_palavra_erros(palavra_secreta, erros)


def mostrar_dica(dicas, contador):
    print(dicas[contador])
    contador += 1
    return contador


def comparar_chute(chute, palavra_chave, palavra_secreta, erros):
    chute = chute.upper()

    palavra_chave = palavra_chave.upper()
    palavra_secreta_nova = list(palavra_secreta)

    acertou = False

    for index in range(0, len(palavra_chave)):
        if chute == palavra_secreta[index]:
            os.system("cls")
            print("Você já chutou essa letra!")
            time.sleep(0.15)
            break
        if palavra_chave[index] == chute:
            palavra_secreta_nova[index] = chute
            acertou = True
        else:
            continue

    if acertou == False:
        erros += 1
        os.system("cls")
        erro()
    else:
        os.system("cls")
        acerto()
        pass

    retorno = [(''.join(palavra_secreta_nova)), erros]
    return retorno


def op_invalida():
    os.system("cls")
    print("Opção inválida.")
    print("Selecione a opção número 1 ou a número 2")
    time.sleep(2.5)


def exibe_palavra_erros(palavra_secreta, erros):
    print(palavra_secreta)
    print("Erros: " + str(erros))


def acerto():
    acertou = "ACERTOU!"
    for letra in acertou:
        print(letra)
        time.sleep(0.10)


def erro():
    errou = "ERROU!"
    for letra in errou:
        print(letra)
        time.sleep(0.10)


def salva_partida(desafiante, jogador, palavra_chave, vencedor):
    file = open("resultados.txt", "r")
    partidas_anteriores = file.readlines()
    file.close()
    file = open("resultados.txt", "w")
    for item in partidas_anteriores:
        file.write(item)
    if vencedor == "Desafiante":
        file.write("Palavra Chave: " + palavra_chave + " - Vencedor: Desafiante" +
                   desafiante + ", Perdedor: jogador: " + jogador + "\n")
    else:
        file.write("Palavra Chave: " + palavra_chave + " - Vencedor: Jogador" +
                   jogador + ", Perdedor: Desafiante: " + desafiante + "\n")
    file.close()


def exibe_historico():
    file = open("resultados.txt", "r")
    conteudo = file.read()
    print(conteudo)
    file.close()


def jogar_novamente():
    while True:
        try:
            while True:
                jogar = int(input("Deseja jogar novamente? [1] Sim [2] Não: "))
                if jogar == 1:
                    jogar = True
                    return jogar
                    break
                elif jogar == 2:
                    jogar = False
                    return jogar
                    break
                else:
                    print("Insira apenas 1 ou 2!")
        except:
            print("Insira um número!")
        jogar = int(input("Escolha apenas 1 ou 2: "))