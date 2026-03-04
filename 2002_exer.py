cliInfo_Nome = ""
cliInfo_Renda = 0.0
cliInfo_Gasto = 0.0
cliInfo_Confi = 0
cliInfo_Anos = 0
cliInfo_Taxa = 0.0
statusAplic = ""

botPerg = ["Qual o seu Nome?\n", "Qual a sua renda mensal?\n", "Qual seria o valor estimado de seu gasto mensal?\n", "Se pudesse dispor de confiança nos investimentos, quanta seria? (1 ~ 10)\n", "Quantos anos você deseja investir?"]

print(f" << Iniciando Programa do Banco (Modl. P.R.I.M.E) >>")

#   Desconsdere os ID's!!!  Não tem mais esse sistema, era muito complicado......

while (cliInfo_Nome == ""):
    print(f"{botPerg[0]}")
    cliInfo_Nome = str(input(">> ")) # Id de onde está o Nome

while (cliInfo_Renda == 0):
    print(f"{botPerg[1]}")
    cliInfo_Renda = float(input(">> "))# Id de onde está a Renda Mensal

while (cliInfo_Gasto == 0):
    print(f"{botPerg[2]}")
    cliInfo_Gasto = float(input(">> "))# Id de onde está o Gasto Mensal
    
while (cliInfo_Confi == 0):
    print(f"{botPerg[3]}") # Id de onde está o Índice de Confiança
    cliInfo_Confi = int(input(">> "))
    
while (cliInfo_Anos == 0):
    print(f"{botPerg[4]}") # Id de onde está a quantidade de anos EM aplicação
    cliInfo_Anos = int(input(">> "))
    
if (cliInfo_Gasto > cliInfo_Renda):
    print(f"ALERTA! Emergência Financeira!")
else:
    reservaFinan = (cliInfo_Gasto * 6) - cliInfo_Renda
    print(f"Até que o usuário, {cliInfo_Nome}, tenha uma reserva finânceira faltam R${reservaFinan}!")

if (cliInfo_Confi < 4):
    statusAplic = "Tesouro Direto"
elif (cliInfo_Confi >= 4 and cliInfo_Confi <= 7):
    statusAplic = "Fundos Imobiliários"
else: 
    statusAplic = "Ações de Tecnologia"

print(f"O seu perfil, corresponde a uma aplicação em: {statusAplic}")

#Taxas fictícias
if (statusAplic == "Tesouro Direto"):
    cliInfo_Taxa = 1.10
elif (statusAplic == "Fundos Imobiliários"):
    cliInfo_Taxa = 1.25
else:
    cliInfo_Taxa = 1.35

#Simulando uma aplicação
for i in range(cliInfo_Anos):
    cliInfo_Renda = (cliInfo_Anos * cliInfo_Taxa) * cliInfo_Renda
    
print(f"R${cliInfo_Renda:.2f} é a renda estimada para o usuário {cliInfo_Nome}, de acordo com as informações fornecidas.")