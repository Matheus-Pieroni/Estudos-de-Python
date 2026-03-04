salInicial = 1000

#Vai ocorrer um aumento já previsto em 1.5% ou seja

aumentoVal = 0.015

salInicial += aumentoVal * salInicial # O aumento que já aconteceu.

# De 1997 à 2017

data = 1997
while (data <= 2007):
    aumentoVal *= 2
    salInicial += (aumentoVal * salInicial)
    print(f"O salário no ano de {data}, é de R${salInicial:.2f} com um aumento de {aumentoVal:.2f}% no mesmo ano.")
    data += 1