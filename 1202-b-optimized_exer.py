print("Validaçào de pessoas.... Iniciando")

# Variáveis >>
nome = ""
idade = -1
salario = 0
sexo = ""                                                                                                                                                                                                                                                                                               #0_0' nao faz a piada plz

conditionMet = False

def pergunta(var, tipoPerg, textPerg, conditionMet):
    while (conditionMet != True):
        if (conditionMet != True):
            var = tipoPerg(input(textPerg))
            if (var != "" or var != -1):
                conditionMet = True
            else:
                print("Informação inválida")
                continue

pergunta(nome, str, "Qual o teu nome? ", conditionMet)
pergunta(idade, int, "Qual a sua idade? ", conditionMet)
pergunta(idade, float, "Qual o seu salario? ", conditionMet)
pergunta(idade, sexo, "Qual o seu sexo (Biológico)? ", conditionMet)

print("Pessoa cadastrada.")
print("")
print(f"Seus dados: Nome: {nome}; Idade: {idade}; Salario: {salario}; Sexo (bio) : {sexo}")