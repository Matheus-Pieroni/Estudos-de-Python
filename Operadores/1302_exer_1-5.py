print(f" << Utilização de operadores de Identidade >>")

a = [1, 2]
b = [1, 2]

c = a

if (c is a):
    print(f" \"C\" É igual a A!")
else: print(f" \"C\" não é igual a A ")

if (c is b):
    print(f" \"C\" É igual a B!")
else: print(f" \"C\" não é igual a B ")

if (a is not b):
    print(f" \"A\" não é igual a B ")
else: print(f"\"A\" é igual a B")