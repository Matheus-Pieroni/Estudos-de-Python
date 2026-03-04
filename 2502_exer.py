print(f"<< Programa de Vendas - Empresa ZX >>")
print("Insira o nome da filial: ")
nomeFilial = str(input(" >> "))
listaVendas = []
listaLimpa = []
valueBffr = 1

def limpar_dados(listaVendas):
    for i in range(len(listaVendas)):
        if (listaVendas[i] > 0 and listaVendas[i] < 10000):
            listaLimpa.append(listaVendas[i])
        else:
            pass

def analisar_dados(listaLimpa):
    total = 0.0
    media = 0.0
    for i in range(len(listaLimpa)):
        total += listaLimpa[i]
    print(sum(listaLimpa))
    print(len(listaLimpa))
    media = sum(listaLimpa) / int(len(listaLimpa))
    return total, media

def definir_status(media):
    if (media > 5000):
        return "Alta Performance."
    elif (media > 2000 and media < 5000):
        return "Performance Estável."
    else:
        return "Performance Crítica."

while (valueBffr != 0):
    #valueBffr = 0
    valueBffr = float(input("Insira um valor de venda: \n >> "))
    if (valueBffr == 0 and len(listaVendas) == 0):
        print(f"Ei! a lista não pode estar vazia!")
        valueBffr = 1
    elif (valueBffr == 0 and len(listaVendas) != 0):
        continue
    else:
        listaVendas.append(valueBffr)

limpar_dados(listaVendas)

total = analisar_dados(listaLimpa)[0] # Aqui ó
media = analisar_dados(listaLimpa)[1]
print(f" >> SUMÁRIO DA EMPRESA, {nomeFilial} <<")
print(f"\t {nomeFilial}")
print(f"Status Atual: {definir_status(media)}")
print(f"Faturamento Total: {total:.2f}; Média de Vendas: {media:.2f}") # Só considerarei as informações consideradas "Válidas"
print(f"Vendas Consideradas:")
for i in range(len(listaLimpa)):
    print(f"{listaLimpa[i]}")

#tchau tchau