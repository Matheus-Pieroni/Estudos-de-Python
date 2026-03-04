#MODELO DE TUPLA (ID_Produto, Nome, Quantidade, Preço_Unitário).
print(" << Sistema de Processameto de Dados de Vendas >> ")
vendas_brutas = [(101, "Monitor", 5, 1200.0), (102, "Mouse", 50, 80.0), (103,
"Teclado", 8, 150.0), (104, "Case", 3, 50.0)]
estoqueBaixo = []
estoqueReajuste = []
valorInventario = 0.0

for i in range(len(vendas_brutas)):
    if (vendas_brutas[i][2] < 10):
        estoqueBaixo.append(vendas_brutas[i][1])
    valorInventario += (vendas_brutas[i][2] * vendas_brutas[i][3])

for i in range(len(vendas_brutas)):
    if (vendas_brutas[i][2] < 10):
        bufferPreco = vendas_brutas[i][3]
        bufferPreco = bufferPreco + (bufferPreco * 0.15) #Ajuste de 15%
        estoqueReajuste.append((vendas_brutas[i][0], vendas_brutas[i][1], vendas_brutas[i][2], bufferPreco))

print(f"\nItens com estoque baixo: {estoqueBaixo}\n")
print(f"Valor Total do Inventário, R${valorInventario:.2f}\n")

print(f"Itens antes da mudança: {vendas_brutas}")

for i in range(len(estoqueReajuste)):
    #print(f"Item antes da mudança: {estoqueReajuste[i][1]}, Valor: {estoqueReajuste[i][3] - (estoqueReajuste[i][3] * 0.15):.2f}")
    print(f"Item com valor reajustado: {estoqueReajuste[i][1]}, Valor: {estoqueReajuste[i][3]:.2f}\n")