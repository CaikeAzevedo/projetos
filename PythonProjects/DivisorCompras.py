# variáveis
pessoa1 = 0
pessoa2 = 0
pessoa3 = 0
valormerc = 0
valorprod = 0

quantidade = int(input("O supermercado de hoje vai ser feito por quantas pessoas?  "))
if quantidade == 3:
    # uber
    uber1 = float(input("digite o valor do uber: "))
    uber3 = uber1 / 3
    pessoa1 += uber3
    pessoa2 += uber3
    pessoa3 += uber3

    # valor mercado dos 3
    while valorprod != -1:
        valormerc += valorprod
        valorprod = float(input("\ndigite o valor do produto: "))
    valormerc = valormerc / 3
    pessoa1 += valormerc
    pessoa2 += valormerc
    pessoa3 += valormerc

    print("\nvalor dos 3 é igual: ", valormerc + uber3)

    # valor mercado pessoa1 e pessoa2
    valorprod = 0
    valormerc = 0
    tof = input("\nExiste algum(s) produto(s) só da pessoa1 e pessoa2? ")
    if tof == "sim":
        while valorprod != -1:
            valormerc += valorprod
            valorprod = float(input("\ndigite o valor do produto: "))
        valormerc = valormerc / 2
        pessoa1 += valormerc
        pessoa2 += valormerc

    # valor mercado pessoa2 e pessoa3
    valorprod = 0
    valormerc = 0
    tof = input("\nExiste algum(s) produto(s) só da pessoa2 e pessoa3? ")
    if tof == "sim":
        while valorprod != -1:
            valormerc += valorprod
            valorprod = float(input("\ndigite o valor do produto: "))
        valormerc = valormerc / 2
        pessoa2 += valormerc
        pessoa3 += valormerc

    # valor mercado pessoa1 e pessoa3
    valorprod = 0
    valormerc = 0
    tof = input("\nExiste algum(s) produto(s) só da pessoa1 e pessoa3? ")
    if tof == "sim":
        while valorprod != -1:
            valormerc += valorprod
            valorprod = float(input("\ndigite o valor do produto: "))
        valormerc = valormerc / 2
        pessoa1 += valormerc
        pessoa3 += valormerc

    # valor mercado apenas pessoa1
    valorprod = 0
    valormerc = 0
    tof = input("\nExiste algum(s) produto(s) só da pessoa1? ")
    if tof == "sim":
        while valorprod != -1:
            valormerc += valorprod
            valorprod = float(input("\ndigite o valor do produto: "))
        pessoa1 += valormerc

    # valor mercado apenas pessoa2
    valorprod = 0
    valormerc = 0
    tof = input("\nExiste algum(s) produto(s) só da pessoa2? ")
    if tof == "sim":
        while valorprod != -1:
            valormerc += valorprod
            valorprod = float(input("\ndigite o valor do produto: "))
        pessoa2 += valormerc

    # valor mercado apenas pessoa3
    valorprod = 0
    valormerc = 0
    tof = input("\nExiste algum(s) produto(s) só do pessoa3? ")
    if tof == "sim":
        while valorprod != -1:
            valormerc += valorprod
            valorprod = float(input("\ndigite o valor do produto: "))
        pessoa3 += valormerc

    # resultados finais:
    print("\n valor final: ", pessoa1 + pessoa2 + pessoa3)
    print("\npessoa1 tem que pagar: ", pessoa1)
    print("\npessoa2 tem que pagar: ", pessoa2)
    print("\npessoa3 tem que pagar: ", pessoa3)

if quantidade == 2:
    # uber
    uber1 = float(input("digite o valor do uber: "))
    uber2 = uber1 / 2
    pessoa1 += uber2
    pessoa2 += uber2

    # valor mercado dos 2
    while valorprod != -1:
        valormerc += valorprod
        valorprod = float(input("\ndigite o valor do produto: "))
    valormerc = valormerc / 2
    pessoa1 += valormerc
    pessoa2 += valormerc

    print("\nvalor dos 2 é igual: ", valormerc + uber3)

    # valor mercado apenas pessoa1
    valorprod = 0
    valormerc = 0
    tof = input("\nExiste algum(s) produto(s) só da pessoa1? ")
    if tof == "sim":
        while valorprod != -1:
            valormerc += valorprod
            valorprod = float(input("\ndigite o valor do produto: "))
        pessoa1 += valormerc

    # valor mercado apenas pessoa2
    valorprod = 0
    valormerc = 0
    tof = input("\nExiste algum(s) produto(s) só da pessoa2? ")
    if tof == "sim":
        while valorprod != -1:
            valormerc += valorprod
            valorprod = float(input("\ndigite o valor do produto: "))
        pessoa2 += valormerc

    # resultados finais:
    print("\n valor final: ", pessoa1 + pessoa2)
    print("\npessoa1 tem que pagar: ", pessoa1)
    print("\npessoa2 tem que pagar: ", pessoa2)
