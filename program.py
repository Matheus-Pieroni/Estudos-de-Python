print("Programa Iniciando")

def escolha():
    print("Opt 1 - Media de 4 valores")
    print("Opt 2 - coiso")

    opt = float(input("Escolha uma Opção:"))

    match opt:
        case 1:
            print("Opção 1 selecionada")
            mediaHOOWOOW()
        case 2:
            print("Opção 2 selecionada")
            quadrad()
        case 3:
            print("Opção 3 selecionada")
            ICC()
        case 4:
            print("Opção 4 selecionada")
        case default:
            print("Opção inválida")

def mediaHOOWOOW():
    print("Calcule a média de 4 valores")
    v1 = float(input("Digite o valor 1:"))
    v2 = float(input("Digite o valor 2:"))
    v3 = float(input("Digite o valor 3:"))
    v4 = float(input("Digite o valor 4:"))
    result = (v1 + v2 + v3 + v4) / 4
    print("A média é:", result)
    print("Usar o programa novamente? (s/n)")
    resp = str(input("Digite sua escolha:"))
    if resp == "s":
        escolha()
    else:
        print("Programa Encerrado")
        quit()
    
def quadrad():
    print("AS MEDIDAS SÃO EM METROS!")
    lado = float(input("Insira a medida do lado do Retangulo: "))
    base = float(input("Agora, insira a medida da base desse retângulo: "))
    resp = str(input("Agora, a - Área ou p - Perímetro desse retângulo?"))
    match resp:
        case "a":
            result = lado * base
            print("A área vale: ", result)
            
        case "p":
            result = (lado * 2) + (base * 2)
            print("O perímetro vale ", result)
        case default:
            print("Opção errada!")
    quit()

def ICC():
    print("IMC Sério?")
    kg = float(input("Insira o teu peso em kilos:"))
    altura = float(input("Insira a tua altura... EM METROS:"))
    result = kg + (altura ** 2)
    print("Teu IMC vale: ", result)
    if result >= 18.5 or result <= 24.9:
        print("Peso normal...")

escolha()