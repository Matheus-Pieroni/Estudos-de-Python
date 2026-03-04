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