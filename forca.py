def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    print("Fim do jogo")

    palavra_secreta = "banana"
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]

    enforcou = False
    acertou = False

    print(letras_acertadas)
    
    while (not acertou and not enforcou):
        chute = input("Qual a letra? ")
        chute = chute.strip()

        i = 0
        for letra in palavra_secreta:
            if (chute.upper()==letra.upper()):
                letras_acertadas[i] = letra
            print(letras_acertadas)
            i = i + 1
        
if(__name__ == "__main__"):
    jogar()
