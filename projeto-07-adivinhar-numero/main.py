from random import randint

def numero_computador():
    numero_sorteado = randint(1, 100)
    return numero_sorteado

numero_sorteado_computador = numero_computador()

def verificar_numero():
    while True:
        try:
            numero_usuario = int(input("Digite um número entre 1 e 100: "))

            if numero_usuario < 1:
                print("ERRO: Digite apenas números positivos")
            else:
                if numero_usuario <= 100:
                    if numero_usuario > numero_sorteado_computador:
                        print("Muito alto! Tente novamente")
                    elif numero_usuario < numero_sorteado_computador:
                        print("Muito baixo! Tente novamente")
                    else:
                        print(f"Parabéns! Você acertou o número {numero_sorteado_computador}")
                        break
                else:
                    print("Entrada inválida: Número fora do intervalo! Digite um número entre 1 e 100.")
        except ValueError:
            print("Entrada invalida: Por favor digite apenas números")

verificar_numero()
