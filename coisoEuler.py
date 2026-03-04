def fatorial(n): #Inicia uma função que irá calcular o fatorial
    if n < 0: return "Fatorial não existe para negativos" #Caso  valor recebido pela funcao seja negativo ela n irá rodar
    fat = 1 # Define o valor de fatorial para 1, para iniciar tudo
    for i in range(2, n + 1): # se inicia em 2, pois os valores anteriores n possuem um fatorial e será concluido no valor solicitado + 1
        fat *= i #Está parte irá multiplicar o valor anterior pelo novo por exemplo( 2! = 2 ], então 3! = 2.3 = 6, e assim por diante)
    return fat #retorna o valor de fatorial

def Euler():
    e = 0 #Define a variavel
    for n in range(1000): #O máximo que podemos utilizar na computação será 1000, pois acima disto o processamento será lento e ineficiente
        e += 1/fatorial(n) #Nesta parte apenas aplicamos a formula de Euler que é 1/n!
    return e #Retorna o valor de Euler

def Desarranjo(n):
    d = fatorial(n)/Euler() #É a formula padrao para possibilidades de desaranjo
    return d


print(f"{Euler():.50f}")
d = int(input("Você Gostaria de descobrir a possibilidade de desarranjo de quantos itens? \n >> "))
print(f"Você pode desarranjar os {d} objetos em {Desarranjo(d):.0f} possibilidades")
