valorCompra = float(input('Insira o valor da compra: '))
desconto = ''

if (valorCompra > 500.0):
    valorCompra = valorCompra - (valorCompra * 0.30)
    desconto = '30%'
elif (valorCompra > 200.0):
    valorCompra = valorCompra - (valorCompra * 0.20)
    desconto = '20%'
elif (valorCompra > 100.0):
    valorCompra = valorCompra - (valorCompra * 0.10)
    desconto = '10%'
else: 
    #valorCompra = valorCompra 
    desconto = '0%'
    
print(f' A sua compra se resolve em R$ {valorCompra:.2f}, e você recebe um desconto de {desconto}')