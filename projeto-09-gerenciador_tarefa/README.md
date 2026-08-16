# Projeto 09 - Gerenciador de Tarefas

## Sobre

Programa em Python que funciona como um gerenciador simples de tarefas no terminal. O usuário pode adicionar tarefas, visualizar a lista de tarefas cadastradas, remover uma tarefa pelo número e encerrar o programa pelo menu.

O programa também valida entradas inválidas, como letras no lugar de números e opções fora do intervalo permitido.

## Funcionalidades

- Exibe um menu com as opções disponíveis
- Permite adicionar novas tarefas
- Lista todas as tarefas cadastradas com numeração
- Permite excluir uma tarefa pelo número informado
- Valida opções inválidas no menu
- Trata entradas não numéricas
- Exibe mensagens quando a lista está vazia
- Encerra o programa quando o usuário escolhe a opção correta

## Tecnologias

- Python 3

## Estrutura do projeto

```text
projeto-09-gerenciador_tarefa/
├── main.py
└── README.md
```

## Como executar

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
```

2. Acesse a pasta do projeto:
```bash
cd projeto-09-gerenciador_tarefa
```

3. Execute o programa:
```bash
python main.py
```

## Exemplo de uso

```text
1 - Adicionar Tarefa
2 - Listar Tarefas
3 - Excluir Tarefa
4 - Encerrar Programa

Escolha uma opção entre 1 e 4: 1
Digite o nome da tarefa a ser adicionada: estudar python
Tarefa adicionada com sucesso.

Escolha uma opção entre 1 e 4: 2
1 - Estudar python

Escolha uma opção entre 1 e 4: 3
1 - Estudar python
Digite o número da tarefa a ser removida: 1
Tarefa removida com sucesso.

Escolha uma opção entre 1 e 4: 4
Encerrando programa...
```

## Aprendizados

- Criação de funções para separar as responsabilidades do programa
- Uso de listas para armazenar tarefas
- Uso de `while True` para manter o menu em execução
- Uso de `if/elif` para executar ações de acordo com a opção escolhida
- Uso de `enumerate()` para listar tarefas com numeração
- Remoção de itens da lista com `pop()`
- Tratamento de exceções com `try/except`
- Validação de entradas do usuário antes de modificar a lista

---
