#código feito com valores das moedas do dia 18/04/2023 às 11:20

uservalor = int(input("Qual o valor que deseja converter? "))
usermoeda = int(input("Qual moeda você está convertendo? \n1) Real \n2) Dólar \n3) Euro \n"))

moedaretorno = int(input("Para qual moeda você deseja converter? \n1) Real \n2) Dólar \n3) Euro \n"))
conversao = 0

if usermoeda == moedaretorno:
  print("Você precisa selecionar moedas diferentes")

elif usermoeda == 1 and moedaretorno == 2:
  conversao = uservalor // 4.98
  print(f"R${uservalor:,.2f} = US${conversao:,.2f}")

elif usermoeda == 1 and moedaretorno == 3:
  conversao = uservalor / 5.46
  print(f"R${uservalor:,.2f} = €{conversao:,.2f}")

elif usermoeda == 2 and moedaretorno == 1:
  conversao = uservalor * 4.98
  print(f"US${uservalor:,.2f} = RS${conversao:,.2f}")

elif usermoeda == 2 and moedaretorno == 3:
  conversao = uservalor * 0.91
  print(f"US${uservalor:,.2f} = €{conversao:,.2f}")

elif usermoeda == 3 and moedaretorno == 1:
  conversao = uservalor * 5.46
  print(f"€{uservalor:,.2f} = RS${conversao:,.2f}")

elif usermoeda == 3 and moedaretorno == 2:
  conversao = uservalor / 0.91
  print(f"€{uservalor:,.2f} = US${conversao:,.2f}")

