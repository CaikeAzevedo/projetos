import random

print("Olá, eu sou o robô do Bingo\n")
nmax = int(input("Qual o valor máximo das cartelas? "))
print("\nEscolha uma opção:\n")
sorteados = []
jogo = 1

while jogo == 1:
    escolha = int(input(
        "\n1- Randomize um número novo do bingo \n2- Mostre os números que já foram sorteados \n3- Sair do jogo\n\n"))

    if escolha == 1:
        bola = random.randint(1, nmax)
        while bola in sorteados:
            bola = random.randint(1, nmax)
        if bola not in sorteados:
            print("\nO novo número sorteado foi: ", bola)
            sorteados.append(bola)

    if escolha == 2:
        print("\nOs número sorteados são: ", sorteados)

    if escolha == 3:
        jogo = 3

print("\nOBRIGADO POR JOGAR :)")
