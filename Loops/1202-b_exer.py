print("Validaçào de pessoas.... Iniciando")

nome = ""
idade = -1
salario = 0
sexo = ""                                                                                                                                                                                                                                                                                               #0_0' nao faz a piada plz

conditionMet = False

while (conditionMet != True):
    if (conditionMet != True):
        nome = str(input("Insira o seu nome: "))
        if (nome != ""):
            conditionMet = True
        else:
            print("Informação inválida")
            continue

conditionMet = False


while (conditionMet != True):
    if (conditionMet != True):
        idade = int(input("Insira a sua idade: "))
        if (idade >= 0 and idade <= 150):
            conditionMet = True
        else:
            print("Informação inválida")
            continue

conditionMet = False

while (conditionMet != True):
    if (conditionMet != True):
        salario = float(input("Insira o seu salario: "))
        if (salario >= 0 ):
            conditionMet = True
        else:
            print("Informação inválida")
            continue
        
conditionMet = False

while (conditionMet != True):
    if (conditionMet != True):
        sexo = str(input("Insira o seu sexo (Biológico): "))
        if (sexo == "f" or sexo == "m"):
            conditionMet = True
        else:
            print("Informação inválida")
            continue

print("Pessoa cadastrada.")
print("")
print(f"Seus dados: Nome: {nome}; Idade: {idade}; Salario: {salario}; Sexo (bio) : {sexo}")