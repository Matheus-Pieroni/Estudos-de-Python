print(f" << Exercício de Associação >>")

string = "Ciencia de Dados"
letraBusca = "D"

def verifiqueLetra(letraBusca, string):
    if (letraBusca in string):
        print(f" O caractere \"{letraBusca}\", está em \"{string}\"")
    else:
        print(f" O caractere \"{letraBusca}\", não está em \"{string}\"")

verifiqueLetra(letraBusca, string)

print(f"Agora é a sua vez, escreva algo e o python vai verificar se o caractere está na frase!")

print(f"Escreva aonde vai procurar:")
string = str(input(""))
print(f"Escreva o caractere que ele vai procurar:")
letraBusca = str(input(""))

verifiqueLetra(letraBusca, string)