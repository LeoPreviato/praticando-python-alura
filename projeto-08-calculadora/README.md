# Projeto 08 - Calculadora

## Sobre

Programa em Python que funciona como uma calculadora simples no terminal. O usuário informa dois números e escolhe uma operação matemática entre soma, subtração, multiplicação e divisão.

O programa também valida entradas inválidas, como letras no lugar de números, operadores não permitidos e divisão por zero.

## Funcionalidades

- Solicita dois números ao usuário
- Permite escolher uma das quatro operações básicas:
  - Soma (`+`)
  - Subtração (`-`)
  - Multiplicação (`*`)
  - Divisão (`/`)
- Exibe o resultado da operação escolhida
- Valida operadores inválidos
- Trata entradas não numéricas
- Impede divisão por zero

## Tecnologias

- Python 3

## Estrutura do projeto

```text
projeto-08-calculadora/
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
cd projeto-08-calculadora
```

3. Execute o programa:
```bash
python main.py
```

## Exemplo de uso

```text
Digite o primeiro número: 10
Escolha a operação (+, -, *, /): +
Digite o segundo número: 5

Resultado: 10 + 5 = 15
```

## Aprendizados

- Criação de funções para organizar o código
- Uso de condicionais `if/elif` para escolher a operação matemática
- Validação de opções usando uma lista de operações permitidas
- Tratamento de exceções com `try/except`
- Captura de `ValueError` para entradas inválidas
- Captura de `ZeroDivisionError` para evitar divisão por zero

---
