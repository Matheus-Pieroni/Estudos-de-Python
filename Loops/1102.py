numList = []

for i in range(5):
    response = float(input("Insira um número na lista: "))
    numList.append(response)
    
numList.sort()
print(f"{numList}")