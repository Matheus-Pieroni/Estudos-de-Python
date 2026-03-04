# Exercício 1 

print(" << Programa p/ calculos aritmeticos >>")


int1 = int(input("Insira o primeiro número para ser utilizado nas equações: "))
int2 = int(input("Insira o segundo número para ser utilizado nas equações: "))

resultado = []

def calculosDifiq():
    intermediata = str(f"Soma: {int1 + int2}") 
    resultado.append(intermediata)
    intermediata = str(f" Diferença: {int1 - int2}")
    resultado.append(intermediata)
    intermediata = str(f"Produto: {int1 * int2}")
    resultado.append(intermediata)
    intermediata = str(f"Divisão Real: {int1 / int2}")
    resultado.append(intermediata)
    intermediata = str(f"Divisão Inteira: {int(int1 / int2)}")
    resultado.append(intermediata)
    intermediata = str(f"Resto da Divisão: {int1 % int2}")
    resultado.append(intermediata)

calculosDifiq()

print(f"{resultado}")

# Exercício 1.2

print(f"<< Programa de Saldo >>")

saldo = 1000
valorDeposito = 500
saque = 200

print(f"Seu saldo inicial corresponde a: R${saldo:.2f}")
print(f"Então você recebe um depósito de R${valorDeposito:.2f}")
saldo += valorDeposito
print(f"Seu saldo corresponde agora a: R${saldo:.2f}")
print(f"Mas existem gastos e você deixa para trás: R${saldo:.2f}")
saldo -= saque
print(f"Seu saldo corresponde agora a: R${saldo:.2f}")
print("Ainda assim, você mantém seu saldo aplicado....")
print("E ele rende o dobro do valor anterior!")
saldo *= 2
print(f"Seu saldo ao final de tudo corresponde a: R${saldo:.2f}")

# Exercício 1.3

print(" << Programa de Comparação de Valores >>")

int1 = float(input("Insira o primeiro número para ser utilizado nas equações: "))
int2 = float(input("Insira o segundo número para ser utilizado nas equações: "))

result = 0

igual = False
menor = False
maior = False

result = int1 - int2

match result:
    case 0:
        igual = True
    case -1:
        menor = True
    case 1:
        maior = True

if (menor):
    print(f"O valor {int1:.1f} é menor que {int2:.1f}")
elif (igual):
    print(f"O valor {int1:.1f} é igual ao de {int2:.1f}")
elif (maior):
    print(f"O valor {int1:.1f} é maior que {int2:.1f}")

print("Encerrando programa.......")

# Exercício 1.4

aluno = [] # posições 0 e 1 são as notas, 3 é a presença e 4 é a média

print(f" << Programa Avaliador de Alunos Iniciando... >>")

aluno.append(int(input("Insira a presença do aluno: ")))
aluno.append(float(input("Insira a primeira nota do aluno: ")))
aluno.append(float(input("Insira a segunda nota do aluno: ")))

nota1 = aluno[1]
nota2 = aluno[2]

aluno.append((nota1 + nota2) / 2)

if (aluno[3] >= 7.0 and aluno[0] >= 75):
    aluno.append("Aprovado.")
else:
    aluno.append("Reprovado")
    
print(f"Status do aluno:")
print(f" Presença: {aluno[0]}")
print(f" Nota 1: {aluno[1]}")
print(f" Nota 2: {aluno[2]}")
print(f" Média do aluno: {aluno[3]}")
print(f" Resolução Final sobre o Estudante: {aluno[4]}")

# Exercício 1.5

print(f" << Utilização de operadores de Identidade >>")

a = [1, 2]
b = [1, 2]

c = a

if (c is a):
    print(f" \"C\" É igual a A!")
else: print(f" \"C\" não é igual a A ")

if (c is b):
    print(f" \"C\" É igual a B!")
else: print(f" \"C\" não é igual a B ")

if (a is not b):
    print(f" \"A\" não é igual a B ")
else: print(f"\"A\" é igual a B")

# Exercício 1.6

print(f" << Exercício de Associação >>")

string = "Ciencia de Dados"
letraBusca = "D"

def verifiqueLetra(letraBusca, string):
    if (letraBusca in string):
        print(f" O caractere \"{letraBusca}\", está em \"{string}\"")
    else:
        print(f" O caractere \"{letraBusca}\", não está em \"{string}\"")

verifiqueLetra(letraBusca, string)

print(f"Agora é a sua vez, escreva algo e o python vai verificar se o caractere está na frase!")

print(f"Escreva aonde vai procurar:")
string = str(input(""))
print(f"Escreva o caractere que ele vai procurar:")
letraBusca = str(input(""))

verifiqueLetra(letraBusca, string)

# Exercício 2

print(f" << Programa de Classificação de Nadadores >> ")

nadador = []

nadador.append(str(input("Qual o nome do nadador? >> ")))
nadador.append(int(input("Qual a idade do nadador? >> ")))

if (nadador[1] >= 5 and nadador[1] <= 12):
    nadador.append("Infantil")
elif (nadador[1] >= 13 and nadador[1] <= 17):
    nadador.append("Juvenil")
elif (nadador[1] >= 18):
    nadador.append("Adulto")
else:
    nadador.append("Idade Inválida...")

print(f"Nadador: Nome: {nadador[0]}, Idade: {nadador[1]}, Condição: {nadador[2]}")

# Exercício 3

print(f" << Programa Calculador de Tabuadas >> ")

num = int(input("Insira um número para que sua tabuada seja calculada: "))
result = 0

for i in range(10):
    result = num * (i + 1)
    print(f"{num} * {i+1} = {result}")

print(f"Programa Encerrado.")

# Exercício 4

print(">> Jogo - Acerte a Senha <<")

senha = "python123"
userInput = ""

i = 0

while (userInput != senha):
    if (i == 0):
        print(" Tenta adivinhar a \"senha\"! Vamos Lá!")
    else:
        print(f"Ei você errou! A senha não é {userInput}")
    
    userInput = str(input(" Insira a Senha: "))
    i += 1
    
    
    
print(f"Você acertou a senha!")
print("Acesso Permitido.")