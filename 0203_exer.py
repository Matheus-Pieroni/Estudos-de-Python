resp = ""
totalValor = 0.0

print(f" >>> INICIANDO PROGRAMA - ExploPlan...")
nome = input("\nInsira o nome do explorador. \n >>")

# Anot. sobre como isso vai funcionar. Como os passos mais "baixos" levam a passos mais "altos", a gente cria eles de forma decrescente no código para que um chame o outro.

# ACREDITO FIELMENTE QUE OS LOOPS DE PERGUNTA FUNCIONAM (Hora do commentario, 19:26)
def pergLoop(pergunta, respN = "\n", respS = "\n", condiParar = "f"):
    resp = ""
    print(pergunta)
    while (resp == ""):
        resp = input("S - SIM, N - NÃO \n >>")
        if (resp == "s" or resp == "S" or resp == "Y" or resp == "y"):
            print(f"{respS}")
            return "s"
        elif (resp != "n" or resp != "N"):
            print(f"{respN}")
            if (condiParar == "t"):
                quit()
            else:
                return "n"
        else: 
            print(f"\tRESPOSTA INVÁLIDA. TENTE NOVAMENTE.")
            resp == ""

def pergLoopEx(pergunta, respN = "\n", respS = "\n", exemplo = "$EXEMPLO$", condiParar = "f"):
    resp = ""
    print(pergunta)
    while (resp == ""):
        resp = input("\n\n S - SIM // N - NÃO // E - EXEMPLO \n\n >>")
        if (resp == "s" or resp == "S" or resp == "Y" or resp == "y"):
            print(f"{respS}")
            return "s"
        elif (resp == "e" or resp == "E"):
            print(f"{exemplo}")
            resp = ""
            continue
        elif (resp != "n" or resp != "N"):
            print(f"{respN}")
            if (condiParar == "t"):
                quit()
            else:
                return "n"
        else: 
            print(f"\tRESPOSTA INVÁLIDA. TENTE NOVAMENTE.")
            resp == ""

# O PASSO1 É A PRÓPRIA MISSÃO! (Bem, pelo menos pense assim..........)
    
def passo2():
    if (pergLoopEx(pergunta = "HÁ UM OBSTÁCULO FÍSICO NO CAMINHO?", exemplo = "\t(EXEMPLOS: MONTANHA, ROCHA, RAVINA)") == "s"):
        passo3()
    else:
        passo6()

def passo3():
    if (pergLoop("\t TUDO BEM. \n\t AGORA DECIDA, VOCÊ VAI ESCALAR, OU CONTORNAR ESTE OBSTÁCULO?\n (S - CONTORNAR // N - CONTORNAR)", ) == "s"):
        passo4()
    else:
        passo5()

def passo4():
    if (pergLoop("\n\t SUA TRIPULAÇÃO VAI ESCALAR O OBSTÁCULO.\t\n DEPOIS DO PROCESSO, RESPONDA: VOCÊS CONSEGUIRAM OU NÃO?", "QUE PENA, RETORNANDO À BASE (ESPAÇO-NAVE)...", "CONTINUANDO A EXPLORAÇÃO...") == "s"):
        passo6()
    else:
        passo3()

def passo5():
    print(f"\n\t SUA EQUIPE DECIDIU CONTORNAR O OBSTÁCULO, O CAMINHO MAIS SEGURO.")
    passo6()

def passo6():
    if (pergLoopEx("\n\t CONTINUANDO A EXPLORAÇÃO VOCÊS PERCORREM UM TERRITÓRIO QUE PODE TER MINERAIS, PROCURAR POR MINERAIS?", respS = "VOCÊS DECIDEM BUSCAR OS MINERAIS.", exemplo = "\t ALGUNS MINERAIS RAROS CONHECIDOS SÃO, ILMENITA & TERRAS RARAS") == "s"):
        passo7()
    else:
        print(f"\nTUDO BEM, VOCÊS NÃO VÃO ATRÁS DOS MINERAIS...")
        if (pergLoop("VOCÊ QUER SAIR DO PLANETA SEM TENTAR A BUSCA?", "\tQUE PENA, HAVIAM MINERAIS NA ÁREA...") == "s"):
            passo9()
        else:
            passo2()

def passo7():
    totalValor += 200.0
    if (pergLoop("\n\t VOCÊS ENCONTRAM MINERAIS RAROS NO PLANETA, O QUE AUMENTA O VALOR DA PESQUISA. MAS HÁ UMA DUVIDA NA MENTE DOS CIENTÍSTAS... \n\t \"VAMOS CONTINUAR PROCURANDO?\"") == "s"):
        passo2()
    else:
        passo9()

def passo9():
    print(f"Tendo obtido espólios científicos de valor alto, você e sua equipe embarcam na nave, e retornam à Terra. \n\n\t PARABÉNS COMANDANTE! O valor total arrecadado durante a exploração foi de R${totalValor}")

# O PASSO8() era a estrutura de decisão. Que eu implementei de forma diferente.


print(f"\t>> BEM VINDO EXPLORADOR, {nome}! <<")
print(f"ESTE PROGRAMA FOI DESENVOLVIDO PARA AUXILIAR NA SUA MISSÃO.\n É NECESSÁRIO INICIAR O PROCESSO DE ANÁLISE. É UM PROCESSO AUTOMÁTICO E RÁPIDO \n")
pergLoop("\n\n\t >> INICIAR PROCESSO?", "\tENCERRANDO SYS...", "\tINICIANDO ANÁLISE...", "t")

#Analisando... Analisando...
planetNom = "Alphara-7"
print(f"\n\n\t -- Planeta Detectado - {planetNom} \n\n")
#while True:
passo2()