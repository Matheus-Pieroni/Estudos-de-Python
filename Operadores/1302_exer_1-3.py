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