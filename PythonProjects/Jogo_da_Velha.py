#Matriz 3x3

mat = [[0, 0, 0],
       [0, 0, 0],
       [0, 0, 0]]
for l in range(0,3):
    print(l, mat[l])
print('   0  1  2')


#jogabilidade /1
modo = int(input('escolha um modo: 1 para jogador contra a maquina, 2 para jogador contra outro jogador \n'))

while modo == 1:
    posicao_l1 = int(input('selecione a linha que deseja marcar \n'))
    posicao_c1 = int(input('selecione a coluna que deseja marcar \n'))

    if mat[posicao_l1][posicao_c1] == 0:
        mat[posicao_l1][posicao_c1] = 1
        for l in mat:
            print(l)


#vitorias do jogador 1

    if mat[0][0] == mat[0][1] and mat[0][1] == mat[0][2] and mat[0][2] == 1:
        print('Jogador 1 ganhou o jogo')
        modo = 0
        break

    if mat[1][0] == mat[1][1] and mat[1][1] == mat[1][2] and mat[1][2] == 1:
        print('Jogador 1 ganhou o jogo')
        modo = 0
        break

    if mat[2][0] == mat[2][1] and mat[2][1] == mat[2][2] and mat[2][2] == 1:
        print('Jogador 1 ganhou o jogo')
        modo = 0
        break

    if mat[0][0] == mat[1][0] and mat[1][0] == mat[2][0] and mat[2][0] == 1:
        print('Jogador 1 ganhou o jogo')
        modo = 0
        break

    if mat[0][1] == mat[1][1] and mat[1][1] == mat[2][1] and mat[2][1] == 1:
        print('Jogador 1 ganhou o jogo')
        modo = 0
        break

    if mat[0][2] == mat[1][2] and mat[1][2] == mat[2][2] and mat[2][2] == 1:
        print('Jogador 1 ganhou o jogo')
        modo = 0
        break

    if mat[0][0] == mat[1][1] and mat[1][1] == mat[2][2] and mat[2][2] == 1:
        print('Jogador 1 ganhou o jogo')
        modo = 0
        break

    if mat[0][2] == mat[1][1] and mat[1][1] == mat[2][0] and mat[2][0] == 1:
        print('Jogador 1 ganhou o jogo')
        modo = 0
        break

    print('\n eh a vez da maquina \n')

#jogabilidade /2

    import random

    posicao_l2 = random.randint(0, 2)
    posicao_c2 = random.randint(0, 2)

    while mat[posicao_l2][posicao_c2] != 0:
        posicao_l2 = random.randint(0, 2)
        posicao_c2 = random.randint(0, 2)

    mat[posicao_l2][posicao_c2] = 2
    for l in mat:
        print(l)


#vitórias do jogador 2

    if mat[0][0] == mat[0][1] and mat[0][1] == mat[0][2] and mat[0][2] == 2:
        print('Jogador 2 ganhou o jogo')
        modo = 0
        break

    if mat[1][0] == mat[1][1] and mat[1][1] == mat[1][2] and mat[1][2] == 2:
        print('Jogador 2 ganhou o jogo')
        modo = 0
        break

    if mat[2][0] == mat[2][1] and mat[2][1] == mat[2][2] and mat[2][2] == 2:
        print('Jogador 2 ganhou o jogo')
        modo = 0
        break

    if mat[0][0] == mat[1][0] and mat[1][0] == mat[2][0] and mat[2][0] == 2:
        print('Jogador 2 ganhou o jogo')
        modo = 0
        break

    if mat[0][1] == mat[1][1] and mat[1][1] == mat[2][1] and mat[2][1] == 2:
        print('Jogador 2 ganhou o jogo')
        modo = 0
        break

    if mat[0][2] == mat[1][2] and mat[1][2] == mat[2][2] and mat[2][2] == 2:
        print('Jogador 2 ganhou o jogo')
        modo = 0
        break

    if mat[0][0] == mat[1][1] and mat[1][1] == mat[2][2] and mat[2][2] == 2:
        print('Jogador 2 ganhou o jogo')
        modo = 0
        break

    if mat[0][2] == mat[1][1] and mat[1][1] == mat[2][0] and mat[2][0] == 2:
        print('Jogador 2 ganhou o jogo')
        modo = 0
        break


while modo == 2:
#jogador 1
    posicao_l1 = int(input('selecione a linha que deseja marcar \n'))
    posicao_c1 = int(input('selecione a coluna que deseja marcar \n'))


    if mat[posicao_l1][posicao_c1] == 0:
        mat[posicao_l1][posicao_c1] = 1
        for l in mat:
            print(l)

#vitorias do jogador 1
    if mat[0][0] == mat[0][1] and mat[0][1] == mat[0][2] and mat[0][2] == 1:
        print('Jogador 1 ganhou o jogo')
        modo = 0
        break

    if mat[1][0] == mat[1][1] and mat[1][1] == mat[1][2] and mat[1][2] == 1:
        print('Jogador 1 ganhou o jogo')
        modo = 0
        break

    if mat[2][0] == mat[2][1] and mat[2][1] == mat[2][2] and mat[2][2] == 1:
        print('Jogador 1 ganhou o jogo')
        modo = 0
        break

    if mat[0][0] == mat[1][0] and mat[1][0] == mat[2][0] and mat[2][0] == 1:
        print('Jogador 1 ganhou o jogo')
        modo = 0
        break

    if mat[0][1] == mat[1][1] and mat[1][1] == mat[2][1] and mat[2][1] == 1:
        print('Jogador 1 ganhou o jogo')
        modo = 0
        break

    if mat[0][2] == mat[1][2] and mat[1][2] == mat[2][2] and mat[2][2] == 1:
        print('Jogador 1 ganhou o jogo')
        modo = 0
        break

    if mat[0][0] == mat[1][1] and mat[1][1] == mat[2][2] and mat[2][2] == 1:
        print('Jogador 1 ganhou o jogo')
        modo = 0
        break

    if mat[0][2] == mat[1][1] and mat[1][1] == mat[2][0] and mat[2][0] == 1:
        print('Jogador 1 ganhou o jogo')
        modo = 0
        break

#jogador 2
    posicao_l2 = int(input('selecione a linha que deseja marcar \n'))
    posicao_c2 = int(input('selecione a coluna que deseja marcar \n'))

    if mat[posicao_l2][posicao_c2] == 0:
        mat[posicao_l2][posicao_c2] = 2
        for l in mat:
            print(l)

#vitorias do jogador 2
    if mat[0][0] == mat[0][1] and mat[0][1] == mat[0][2] and mat[0][2] == 2:
        print('Jogador 2 ganhou o jogo')
        modo = 0
        break

    if mat[1][0] == mat[1][1] and mat[1][1] == mat[1][2] and mat[1][2] == 2:
        print('Jogador 2 ganhou o jogo')
        modo = 0
        break

    if mat[2][0] == mat[2][1] and mat[2][1] == mat[2][2] and mat[2][2] == 2:
        print('Jogador 2 ganhou o jogo')
        modo = 0
        break

    if mat[0][0] == mat[1][0] and mat[1][0] == mat[2][0] and mat[2][0] == 2:
        print('Jogador 2 ganhou o jogo')
        modo = 0
        break

    if mat[0][1] == mat[1][1] and mat[1][1] == mat[2][1] and mat[2][1] == 2:
        print('Jogador 2 ganhou o jogo')
        modo = 0
        break

    if mat[0][2] == mat[1][2] and mat[1][2] == mat[2][2] and mat[2][2] == 2:
        print('Jogador 2 ganhou o jogo')
        modo = 0
        break

    if mat[0][0] == mat[1][1] and mat[1][1] == mat[2][2] and mat[2][2] == 2:
        print('Jogador 2 ganhou o jogo')
        modo = 0
        break

    if mat[0][2] == mat[1][1] and mat[1][1] == mat[2][0] and mat[2][0] == 2:
        print('Jogador 2 ganhou o jogo')
        modo = 0
        break