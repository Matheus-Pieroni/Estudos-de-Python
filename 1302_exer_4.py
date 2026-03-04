print(">> Jogo - Acerte a Senha <<")

senha = "python123"
userInput = ""

i = 0

while (userInput != senha):
    if (i == 0):
        print(" Tenta adivinhar a \"senha\"! Vamos Lá!")
    else:
        print(f"Ei você errou! A senha não é {userInput}")
    
    userInput = str(input(" Insira a Senha: "))
    i += 1
    
    
    
print(f"Você acertou a senha!")
print("Acesso Permitido.")