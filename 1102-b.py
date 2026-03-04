iteratorIni = int(input("Escolha um número base pro iterador: "))
iteratorFin = int(input("Escolha um número limite pro iterador: "))

if (iteratorIni <= iteratorFin):
    for iteratorIni in range(iteratorFin):
        print(iteratorIni)
else:
    for iteratorFin in range(iteratorIni):
        print(iteratorFin)
    