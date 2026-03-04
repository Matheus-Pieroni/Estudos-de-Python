print(f" << Programa de Classificação de Nadadores >> ")

nadador = []

nadador.append(str(input("Qual o nome do nadador? >> ")))
nadador.append(int(input("Qual a idade do nadador? >> ")))

if (nadador[1] >= 5 and nadador[1] <= 12):
    nadador.append("Infantil")
elif (nadador[1] >= 13 and nadador[1] <= 17):
    nadador.append("Juvenil")
elif (nadador[1] >= 18):
    nadador.append("Adulto")
else:
    nadador.append("Idade Inválida...")

print(f"Nadador: Nome: {nadador[0]}, Idade: {nadador[1]}, Condição: {nadador[2]}")