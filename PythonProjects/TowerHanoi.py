def torredehanoi(n, pino1, pino2, pino3):
    if n == 1:
        print("Mover disco 1 do pino", pino1, "para o pino", pino2)
        return
    torredehanoi(n - 1, pino1, pino3, pino2)
    print("Mover disco", n, "do pino", pino1, "para o pino", pino2)
    torredehanoi(n - 1, pino3, pino2, pino1)


n = int(input("com quantos pinos quer jogar?"))
torredehanoi(n, 'A', 'C', 'B')
