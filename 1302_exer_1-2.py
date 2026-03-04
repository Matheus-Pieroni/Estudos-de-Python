print(f"<< Programa de Saldo >>")

saldo = 1000
valorDeposito = 500
saque = 200

print(f"Seu saldo inicial corresponde a: R${saldo:.2f}")
print(f"Então você recebe um depósito de R${valorDeposito:.2f}")
saldo += valorDeposito
print(f"Seu saldo corresponde agora a: R${saldo:.2f}")
print(f"Mas existem gastos e você deixa para trás: R${saldo:.2f}")
saldo -= saque
print(f"Seu saldo corresponde agora a: R${saldo:.2f}")
print("Ainda assim, você mantém seu saldo aplicado....")
print("E ele rende o dobro do valor anterior!")
saldo *= 2
print(f"Seu saldo ao final de tudo corresponde a: R${saldo:.2f}")