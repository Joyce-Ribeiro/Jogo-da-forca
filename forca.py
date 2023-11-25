import random
from unidecode import unidecode

def imprime_mensagem_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

def carrega_palavra_secreta():
    arquivo = open('jogos/palavras.txt', "r")
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    
    arquivo.close()

    numero = random.randrange(0, len(palavras))

    palavra_secreta = palavras[numero].upper()

    return palavra_secreta.upper()

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def remove_acentos(letra):
    if letra == 'Ç':
        return letra
    return unidecode(letra)

def jogar():
    imprime_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0
    print(palavra_secreta)
    while (not acertou and not enforcou):
        print(letras_acertadas)
        chute = input("Qual a letra? ")
        chute = remove_acentos(chute.strip().upper())
        if(chute in palavra_secreta):
            i = 0
            for letra in palavra_secreta:
                if (chute==remove_acentos(letra)):
                    letras_acertadas[i] = letra
                i = i + 1
        else:
            erros = erros + 1
        
        enforcou = erros == 6
        acertou = "_" not in letras_acertadas

    if(acertou):
        print("Você ganhou!!")
    else:
        print("Você perdeu!!")

    print("Fim do jogo")
if(__name__ == "__main__"):
    jogar()
