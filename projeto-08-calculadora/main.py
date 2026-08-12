def calculadora():
    lista_operacoes = ["+", "-", "*", "/"]
    try:
        valor1 = int(input("Digite o primeiro número: "))
        operacao = input("Escolha a operação (+, -, *, /): ").strip()
        if operacao not in lista_operacoes:
            print("\nOpção inválida. Digite apenas (+, -, *, /).")
            return
        valor2 = int(input("Digite o segundo número: "))

        if operacao == "+":
            resultado = valor1 + valor2
            print(f"\nResultado: {valor1} + {valor2} = {resultado}")
        elif operacao == "-":
            resultado = valor1 - valor2
            print(f"\nResultado: {valor1} - {valor2} = {resultado}")
        elif operacao == "*":
            resultado = valor1 * valor2
            print(f"\nResultado: {valor1} * {valor2} = {resultado}")
        elif operacao == "/":
            resultado = valor1 / valor2
            print(f"\nResultado: {valor1} / {valor2} = {resultado}")

    except ValueError:
        print("\nERRO: Entrada inválida. Digite apenas números.")
    except ZeroDivisionError:
        print("\nERRO: Divisão por zero não é permitida.")

calculadora()