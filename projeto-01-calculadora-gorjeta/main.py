def calcular_gorjeta(valor_conta, porcentagem):
    return valor_conta * (porcentagem / 100)

def ler_valor_conta(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            if valor <= 0:
                print("O valor não pode ser zero ou negativo. Tente novamente.")
                continue
            return valor
        except ValueError:
            print(
            "ERRO! Digite apenas números."
            )
            
def ler_valor_gorjeta(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            if valor < 0:
                print("O valor não pode ser negativo. Tente novamente.")
                continue
            return valor
        except ValueError:
            print(
            "ERRO! Digite apenas números."
            )

total_conta = ler_valor_conta("Total a pagar: R$ ")
gorjeta = ler_valor_gorjeta("Porcentagem de gorjeta: ")

total_gorjeta = calcular_gorjeta(total_conta, gorjeta)

print()
print(f"Valor da gorjeta: R$ {total_gorjeta:.2f}")
print(f"Total a pagar: R$ {total_conta + total_gorjeta:.2f}")
