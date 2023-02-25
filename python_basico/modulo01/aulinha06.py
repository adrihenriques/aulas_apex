from time import sleep 
#sleep usamos para controlar  o time
nome = input("digite seu nome:>")
sobrenome = input("digite seu sobrenome")
idade = int(input("digite sua idade"))


for lista in range(0,2):
    nota = int(input("digite a sua:>"))

    lista_nota = [nota]

    media = sum(lista_nota)/ len(lista_nota)

situacao = "reprovado tente novamente"

if media >= 7:
    sleep(2)
    for c in range(0,10):
        print("*")
        sleep(1)
    situacao = "parabens voce foi aprovado"

dicionario = {"nome" : nome, "sobrenome" : sobrenome, "idade" : idade, "media" : media, "situacao" : situacao}

print(f"{dicionario['nome']} {dicionario['sobrenome']}{dicionario['idade']} {dicionario['situacao']}")