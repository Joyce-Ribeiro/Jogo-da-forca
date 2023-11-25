import random
def jogar():
    arquivo = open("palavras.txt", "r")
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    
    arquivo.close()

    numero = random.randrange(0, len(palavras))

    palavra_secreta = palavras[numero].upper()

    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    print("Fim do jogo")

    palavra_secreta = "banana"
    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0
    
    while (not acertou and not enforcou):
        print(letras_acertadas)
        chute = input("Qual a letra? ")
        chute = chute.strip()
        if(chute in palavra_secreta):
            i = 0
            for letra in palavra_secreta:
                if (chute.upper()==letra.upper()):
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

if(__name__ == "__main__"):
    jogar()
