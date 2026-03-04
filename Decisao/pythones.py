print("Programa iniciando...")
print(" -- Programa de Média em python -- ")

nota1 = float(input("Insira a primeira nota: "))
nota2 = float(input("Insira a segunda nota: "))

media = (nota1 + nota2) / 2

if (media >= 7):
    print(f"Parabéns! Você foi aprovado com a média: {media}")
else:
    print(f"Ei, você foi reprovado com a média: {media}")