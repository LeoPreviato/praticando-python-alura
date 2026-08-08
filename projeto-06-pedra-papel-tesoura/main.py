from random import choice

opcoes = ["Pedra", "Papel", "Tesoura"]

def escolha_computador():
    escolhido = choice(opcoes)
    return escolhido

def escolha_usuario():
    while True:
        opcao_escolhida = input("Escolha Pedra, Papel ou Tesoura: ").strip().capitalize()

        if opcao_escolhida not in opcoes:
            print(f"ERRO: Opção invalida. Escolha Pedra, Papel ou Tesoura.")
            continue
        else:
            return opcao_escolhida

def verificar_ganhador(escolhido_usuario, escolhido_computador):
    if escolhido_usuario == escolhido_computador:
        return "Empate!"
    elif (
        (escolhido_usuario == "Pedra" and escolhido_computador == "Tesoura") or
        (escolhido_usuario == "Papel" and escolhido_computador == "Pedra") or
        (escolhido_usuario == "Tesoura" and escolhido_computador == "Papel")
    ):
        return "Você Venceu!"
    else:
        return "Você Perdeu!"

usuario = escolha_usuario()
computador = escolha_computador()

print(f"O computador escolheu: '{computador}'")
print(verificar_ganhador(usuario, computador))
