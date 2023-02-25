
#importaçao otimizada,quando eu importo o modelo e a funçao
from random import choice

n1 = input("Digite seu nome")
n2 = input("Digite seu nome")
n3 = input("Digite seu nome")
n4 = input("Digite seu nome")


lista =[n1,n2,n3,n4]

sorteado = choice(lista)

print(" "*20, "Nome Sorteado", " "*20)

print(f"{sorteado}")


if sorteado == n1:
    print("o nome sorteado foi o primeiro digitado")
if sorteado == n2:
    print("o nome sorteado foi o segundo digitadom")
if sorteado == n3:
    print("o nome sorteado foi o terceiro digitadom")
if sorteado == n4:
    print("o nome sorteado foi o quarto digitadom")
