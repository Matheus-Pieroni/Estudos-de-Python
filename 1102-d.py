numList = []
final = 0.0

for i in range(5):
    numList.append(float(input(f"Insira um número para a posição {i+1}: ")))

for i in range(len(numList)):
    final += numList[i]

finalVal = final / len(numList)

print(f"E a média é: {finalVal}")