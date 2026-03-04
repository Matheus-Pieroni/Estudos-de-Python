print(f" << Programa Calculador de Tabuadas >> ")

num = int(input("Insira um número para que sua tabuada seja calculada: "))
result = 0

for i in range(10):
    result = num * (i + 1)
    print(f"{num} * {i+1} = {result}")

print(f"Programa Encerrado.")