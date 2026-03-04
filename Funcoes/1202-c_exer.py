encerraCompra = 0.00

preco = 0.00

precoAdd = 1.00

def encerrarCompra(preco):
    resp = ""
    print("Qual vai ser o método de pagamento?")
    resp = str(input("C - Crédito, D - Débito: "))
    match resp:
        case "c":
            print(f"Tudo bem...")
            print(f"Valor final: R$ {preco}")
            
        case "d":
            print(f"Tudo bem...")
            print(f"... Você está elegível para um desconto de 5%!")
            preco = preco - (preco * 0.05)
            print(f"Preço final: {preco:.2f}")
        case default:
            print(f"Resposta inválida.")
            

def coisoComprar(preco, precoAdd, encerraCompra):
    while (precoAdd != encerraCompra):
        if (precoAdd <= -1):
            print("Valor Inválido!")
        else:
            precoAdd = float(input("Adicione o valor do item ao carrinho: "))
            preco += precoAdd
    
    if (precoAdd == 0):
        resp = ""
        print("Você realmente deseja encerrar a compra?")
        resp = str(input("S - Sim, N - Não: "))
        resp.lower()
        match resp:
            case "s":
                encerrarCompra(preco)
            case "n":
                coisoComprar(preco, precoAdd, encerraCompra)
            case default:
                print(f"O valor inserido como resposta, \"{resp}\", é inválido...")
                print(f"Encerrando o programa.")
   
coisoComprar(preco, precoAdd, encerraCompra)