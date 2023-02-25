choop = float(input("digite quantos choops você bebeu na ocktober"))

if choop == 0: 
   print("você nâo bebeu")

elif choop ==  1  and choop <=5:
    print("você esta na zona de risco!")
    multa = choop * 100 
elif choop > 5 :
    print("você ja esta alterado!") 
    multa = choop * 100

#imprimir multa
    print(f"o valor da multa é R${multa}")
