lista_tarefa = []

def menu_opcoes():
    print("""
1 - Adicionar Tarefa
2 - Listar Tarefas
3 - Excluir Tarefa
4 - Encerrar Programa    
""")

def escolher_opcao():
    while True:
        try:
            opcao_usuario = int(input("Escolha uma opção entre 1 e 4: "))

            if opcao_usuario < 1 or opcao_usuario > 4:
                print("ERRO: Escolha uma opção entre 1 e 4.")

            if opcao_usuario == 1:
                adicionar_tarefa()
            elif opcao_usuario == 2:
                listar_tarefas()
            elif opcao_usuario == 3:
                excluir_tarefa()
            elif opcao_usuario == 4:
                encerrar_programa()
        except ValueError:
            print("ERRO: Digite apenas números.")

def adicionar_tarefa():
    nome_tarefa = input("Digite o nome da tarefa a ser adicionada: ").strip().capitalize()
    lista_tarefa.append(nome_tarefa)

    print("Tarefa adicionada com sucesso.")

def listar_tarefas():
    if lista_tarefa:
        for indice, tarefa in enumerate(lista_tarefa):
            print(f"{indice+1} - {tarefa}")
    else:
        print("ERRO: Nenhuma tarefa adicionada na lista.")

def excluir_tarefa():
    if len(lista_tarefa) == 0:
        print("ERRO: Lista de tarefas vazia.")
        return

    listar_tarefas()

    try:
        numero_tarefa = int(input("Digite o número da tarefa a ser removida: "))

        if numero_tarefa < 1 or numero_tarefa > len(lista_tarefa):
            print("ERRO: Número de tarefa inválido.")
            return

        lista_tarefa.pop(numero_tarefa - 1)
        print("Tarefa removida com sucesso.")
    except ValueError:
        print("ERRO: Digite apenas o número da tarefa.")

def encerrar_programa():
    print("Encerrando programa...")
    quit()

def main():
    while True:
        menu_opcoes()
        escolher_opcao()

main()