def calcular_gorjeta(valor_conta, porcentagem):
    return valor_conta * (porcentagem / 100)

total_conta = float(input("Total a pagar: R$ "))
gorjeta = int(input("Porcentagem de gorjeta: "))

total_gorjeta = calcular_gorjeta(total_conta, gorjeta)

print()

print(f"Valor da gorjeta: R$ {total_gorjeta:.2f}")
print(f"Total a pagar: R$ {total_conta + total_gorjeta:.2f}")