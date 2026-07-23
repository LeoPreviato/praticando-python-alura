# Projeto 04 - Identificador de Palavras Longas

## 📖 Sobre

Este programa recebe um texto informado pelo usuário e identifica todas as palavras que possuem mais de 10 letras, exibindo-as em destaque. A ideia parte de um cenário prático: Sofia, revisora de textos, precisa localizar palavras muito longas em um parágrafo, já que textos com palavras mais curtas costumam ser mais fáceis de ler.

## 🚀 Funcionalidades

- Recebe um texto digitado pelo usuário.
- Divide o texto em palavras.
- Percorre cada palavra verificando seu tamanho.
- Identifica as palavras com mais de 10 letras.
- Exibe as palavras longas encontradas.
- Avisa o usuário caso nenhuma palavra longa seja encontrada.

## 🛠️ Tecnologias utilizadas

- Python 3

## 📂 Estrutura do projeto

```text
projeto-04-identificador-palavras-longas
├── main.py
└── README.md
```

## ▶️ Como executar

1. Clone este repositório:

```bash
git clone <URL_DO_REPOSITORIO>
```

2. Acesse a pasta do projeto:

```bash
cd projeto-04-identificador-palavras-longas
```

3. Execute o programa:

```bash
python main.py
```

## 💻 Exemplo de uso

**Entrada**

```text
Digite um texto: A programação estruturada facilitou o desenvolvimento de grandes sistemas computacionais
```

**Saída**

```text
Palavras longas encontradas: programação, estruturada, desenvolvimento, computacionais
```

**Caso sem palavras longas**

```text
Digite um texto: O gato subiu no telhado
```

```text
Nenhuma palavra longa foi encontrada no texto
```

## 📚 Aprendizados

Neste projeto pratiquei:

- Criação de funções.
- Percorrer listas com `for`.
- Manipulação de texto com `split()` e `strip()`.
- Estruturas condicionais.
- Formação de listas e verificação de tamanho de strings.
- Formatação de saída com f-strings e `join()`.

---

Projeto desenvolvido para fins de estudo durante os cursos da **Alura**.