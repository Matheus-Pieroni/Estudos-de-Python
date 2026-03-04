print(f" << Empresa X - Processador de Transações >>")

# Limpa Consoles... >> print("\033c", end="")

saldoInicial = 1000.0
caracteresProibidos = "~!@#$%^&*|?/':;<>.,_-¿´¶«»¬×¥’‘¾½¼€¤³²¡¹£÷¦°¨0123456789"
checkpoint = saldoInicial
nomeAudit = ""

def limpaConsole():
    print(f"\033c", end="")

# Exercício 1
if (checkpoint is saldoInicial):
    print(f"\"checkPoint == saldoInicial\" = {saldoInicial is checkpoint}")
    print(f" A variável retornou verdadeiro para o passo 1, continuando....")
    
# Exercício 2
i = 0
while (nomeAudit == ""):
    nomeAudit = str(input("""Insira o nome do Auditor:
    >> """))                    # ta dando erro poxa...
    while (i != len(nomeAudit)):
        if (nomeAudit[i] in caracteresProibidos):
            print(f"Há caracteres proibidos no nome do auditor, \"{nomeAudit[i]}\" por favor tente novamente.")
            nomeAudit = ""
            i = 0
            continue
        else:
            print(f"Caractére em \"Nome do Auditor\", \"{nomeAudit[i]}\" Aceito, prosseguindo....")
            i += 1
limpaConsole()
print(f" Bem-Vindo Auditor, {nomeAudit}\n")


# Exercício 3
saldo = saldoInicial
print(" -- Iniciando Operador de Transações -- ")
valorBuffer = 0
for i in range(4): # Se colocar 3 ele repete só três vezes. Nã0 é como parece...
    print(f"""Método de Operação >>
    Valor Positivo - Para Aplicação de Crédito
    Valor Negativo -  Para Aplicação de Débito""")
    valorAdd = float(input("""Insira o valor a ser adicionado ou decrescido ao saldo
    >> """))
    if ((saldo + valorAdd) <= 0):
        print("O valor de saldo não cobre a transação, continuando sem realizar a operação...")
        print(f"Saldo atual equivalente a: {saldo}")
    elif (valorAdd >= 500.0): 
        print(f"ATENÇÃO! \nTRANSAÇÃO DE ALTO VALOR OCORRENDO! ")
        saldo = saldo + valorAdd
        print(f"Saldo atual equivalente a: {saldo}\n")
    else:
        saldo = saldo + valorAdd
        print(f"Saldo atual equivalente a: {saldo}\n")
limpaConsole()
    
# Exercício 4 ~ 5
print(f"Saldo final equivalente a: {saldo}\n")
if (saldo is checkpoint):
    print(f"O objeto \"Valor final\", {saldo}, se manteve o mesmo objeto que \"checkpoint\".")
    print(f"ID de \"saldo\": {id(saldo)}, ID de \"checkpoint\": {id(checkpoint)}")
else:
    print(f"O objeto \"Valor final\", {saldo}, não se manteve o mesmo objeto que \"checkpoint\".")
    print(f"ID de \"saldo\": {id(saldo)}, ID de \"checkpoint\": {id(checkpoint)}")