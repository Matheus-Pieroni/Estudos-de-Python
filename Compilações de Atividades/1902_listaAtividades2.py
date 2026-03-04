escolhaExer = int(input(f"Escolha o Exercício: (1 - 4)"))

ITALIC = '\x1B[3m'
RESET = '\x1B[0m'

# Exercícios!

def exercicio1():
    status = ["Abaixo do Peso", "Peso Normal", "Sobrepeso", "Obeso"]

    print(f" << Programa de Classificação de IMC >>")

    pesoAgr = float(input("Insira o seu peso, em kg: "))
    alturaAgr = float(input("Insira a sua altura, em metros: "))

    result = pesoAgr / (alturaAgr*2)

    if (result < 18.5):
        print(f"Seu IMC corresponde a {result:.2f}, e você foi classificado como {status[0]}")
    elif (result >= 18.5 or result <= 24.9):
        print(f"Seu IMC corresponde a {result:.2f}, e você foi classificado como {status[1]}")
    elif ( result >= 25.0 or result <= 29.9):
        print(f"Seu IMC corresponde a {result:.2f}, e você foi classificado como {status[2]}")
    else:
        print(f"Seu IMC corresponde a {result:.2f}, e você foi classificado como {status[3]}")

def exercicio2():
    print(f"  << Programa de Verificação de Vogais... {ITALIC}sério?{RESET}")\
    
    vogais = []
    strDeVerif = "aeiouAEIOU"
    vogaisEncontradas = 0
    
    nome = str(input("Insira um nome, para que ocorra a verificação: "))
    
    for i in range(len(nome)):
        if (nome[i] in strDeVerif):
            vogais.append(nome[i])
            vogaisEncontradas += 1
            
    print(f" Total de vogais encontradas: {vogaisEncontradas} vogais.")
    print(f"{vogais}")

def exercicio3():
    print("<< Programa de Operações Bancárias >> {ITALIC} quem me dera {RESET}")
    saldo = 500.0
    valor = 0
    escolha = 0
    
    print("Opções:")
    while (escolha == 0):
        print(f" Saldo depois da operação: {saldo}")
        print("")
        print("1 - Deposito")
        print("2 - Sacar")
        print("3 - Sair")
        escolha = int(input("Sua escolha: "))
        
        if (escolha == 1):
            print(f" >> Serviço de Depósitos")
            print(f" Este é seu saldo atual: {saldo}")
            valDeposito = float(input("""Qual o valor do depósito?
 >> """))
            saldo += valDeposito
            escolha = 0 
        elif (escolha == 2):
            print(f" >> Serviço de Saque")
            print(f" Este é seu saldo atual: {saldo}")
            valSaque = float(input("""Qual o valor do saque?
 >> """))
            saldo -= valSaque
            escolha = 0
        else:
            escolha = 1
        print(f"Obrigado por usar o serviço.")
    
def exercicio4():
    print(f" << Exercício sobre cópia de Dados >>")
    
    dadosOriginais = [10, 20, 30]
    
    print(f"Tabela de dados originais: {dadosOriginais}")
    print("Copiando dados à nova tabela...\n e associando-a a tabela original.")
    
    dadosReferencia = dadosOriginais
    
    print(f"Nova tabela criada. \nPassando dados novos identicos à nova tabela...")
    print(f"{dadosReferencia}")
 
    dadosCopia = [10, 20, 30]
    
    print(f"dadosCopia criado... dadosCopia: {dadosCopia}")
    
    if (dadosReferencia is dadosOriginais):
        print("O objeto dadosRefência é o mesmo objeto que dadosOriginais")
    
    if (dadosCopia is dadosOriginais):
        print("O objeto dadosCopia é o mesmo objeto que dadosOriginais")
    else:
        print("O objeto dadosCopia não é o mesmo objeto que dadosOriginais")
    
match escolhaExer:
    case 1:
        exercicio1()
    case 2:
        exercicio2()
    case 3:
        exercicio3()
    case 4:
        exercicio4()
    case default:
        print(f" {ITALIC}Escolha Incorreta...{RESET} Por favor escolha corretamente, o objetivo da ativ. é ver os Exer's funcionando...")