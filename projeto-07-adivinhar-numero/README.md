#  Projeto 07 - Adivinhe o Número

## Sobre

Programa em Python onde o computador sorteia um número aleatório entre 1 e 100, e o jogador precisa tentar adivinhar qual é. A cada tentativa, o programa informa se o palpite está muito alto ou muito baixo, além de validar as entradas do usuário para evitar erros durante a execução.

## Funcionalidades

- Sorteio automático de um número entre 1 e 100
- Feedback ao jogador informando se o palpite foi muito alto ou muito baixo
- Mensagem de vitória exibindo o número correto ao final
- Validação de entradas inválidas:
  - Letras ou caracteres não numéricos
  - Números negativos ou zero
  - Números fora do intervalo de 1 a 100

## Tecnologias

- Python 3
- Módulo `random` (função `randint`)

## Estrutura do projeto

```text
projeto-07-adivinhar-numero/
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
cd projeto-07-adivinhar-numero
```

3. Execute o programa:
```bash
python main.py
```

## Exemplo de uso

```text
Digite um número entre 1 e 100: 50
Muito alto! Tente novamente

Digite um número entre 1 e 100: 25
Muito baixo! Tente novamente

Digite um número entre 1 e 100: 37
Parabéns! Você acertou o número 37
```

## Aprendizados

- Estruturação de um projeto usando o processo de 5 passos (definir problema, organizar passos, estruturar, codar, testar) antes de sair codando
- Uso de `while True` combinado com `break` para controlar o fluxo de repetição até o acerto
- Tratamento de exceções com `try/except` para capturar `ValueError` em entradas não numéricas
- Diferença entre validação com `if/elif/else` e tratamento de exceções, e quando usar cada um
- Cuidado com operadores de comparação encadeados (`and` vs `or`) ao validar intervalos de números

---
