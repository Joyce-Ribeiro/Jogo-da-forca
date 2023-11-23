def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    print("Fim do jogo")

    palavra_secreta = "banana"

    enforcou = False
    acertou = False

    while (not acertou and not enforcou):
        chute = input("Qual a letra? ")
        chute = chute.strip()

        i = 0
        for letra in palavra_secreta:
            if (chute.upper()==letra.upper()):
                print(f'Encontrei a letra {chute} na posição {i}')
            i = i + 1
        
if(__name__ == "__main__"):
    jogar()
