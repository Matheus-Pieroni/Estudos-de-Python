perguntas = ["Telefonou para a Vitima?", "Esteve no local do crime?", "Mora perto da Vitima?", "Devia para a Vitima?", "Já trabalhou com a Vitima?"]

resp = 0

final = 0

classific = ""

def avaliadorDeRespostas(resp):
    if (resp == "s" or "S" or "sim" or "Sim" or "SIM"):
        final += 1
    elif (resp == "n" or "N" or "nao" or "não" or "NAO"):
        final += 0
    else:
        print("Resposta incorreta. Tente Novamente.")

for i in perguntas:
    print(i)
    resp = str(input("Sua resposta: (S / N) "))
   
if (final == 5):
    classific = "Assassínio"
elif (final < 3 ):
    classific = "Cúmplice"
elif (final < 2):
    classific = "Suspeita"
else:
    classific = "Inocente"

print(f"{classific}")
