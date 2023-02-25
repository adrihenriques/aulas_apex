from time import sleep

numero = 0
#estrutura de repetiçao
for indice in range (0,3):

    valor = int(input("digite o numero de indice:>"))
    print(f"o numero digitado é (valor)")

    numero += valor
    print(indice)


#estrutura de condiçao
if numero > 10:
    print(f"a soma dos valores é {numero}")
    print("o valor digitado é maior que dez")

elif numero < 10:
     print(f"a soma dos valores é {numero}")
     print("o valor digitado é igual que dez")

else
    print("o valor digitado é menor que dez")


