numero = int(input("digite o numero que voce deseja a tabuada completa:>"))

for tabuada in range(1,11):
    print("{} X {} = |{} ". format(numero,tabuada, numero*tabuada))