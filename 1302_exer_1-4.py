aluno = [] # posições 0 e 1 são as notas, 3 é a presença e 4 é a média

print(f" << Programa Avaliador de Alunos Iniciando... >>")

aluno.append(int(input("Insira a presença do aluno: ")))
aluno.append(float(input("Insira a primeira nota do aluno: ")))
aluno.append(float(input("Insira a segunda nota do aluno: ")))

nota1 = aluno[1]
nota2 = aluno[2]

aluno.append((nota1 + nota2) / 2)

if (aluno[3] >= 7.0 and aluno[0] >= 75):
    aluno.append("Aprovado.")
else:
    aluno.append("Reprovado")
    
print(f"Status do aluno:")
print(f" Presença: {aluno[0]}")
print(f" Nota 1: {aluno[1]}")
print(f" Nota 2: {aluno[2]}")
print(f" Média do aluno: {aluno[3]}")
print(f" Resolução Final sobre o Estudante: {aluno[4]}")