# Projeto 05 - Gerador de Senha Segura

## 📖 Sobre
Este programa gera senhas aleatórias e seguras, combinando letras maiúsculas, minúsculas, números e caracteres especiais. A ideia parte de um cenário prático: Pedro está desenvolvendo um sistema de cadastro e precisa gerar senhas seguras para os usuários automaticamente.

## 🚀 Funcionalidades
- Gera uma senha aleatória de 12 caracteres.
- Garante pelo menos 1 letra maiúscula.
- Garante pelo menos 1 letra minúscula.
- Garante pelo menos 1 número.
- Garante pelo menos 1 caractere especial.
- Embaralha a posição dos caracteres para maior segurança.
- Exibe a senha gerada ao usuário.

## 🛠️ Tecnologias utilizadas
- Python 3
- Módulo `random`

## 📂 Estrutura do projeto
```text
projeto-05-gerador-senha
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
cd projeto-05-gerador-senha
```
3. Execute o programa:
```bash
python main.py
```

## 💻 Exemplo de uso
**Saída**
```text
Senha gerada: A1b@C3d$E5f&
```

*(a senha muda a cada execução, já que é gerada de forma aleatória)*

## 📚 Aprendizados
Neste projeto pratiquei:
- Criação de funções.
- Uso do módulo `random` (`choice`, `choices` e `shuffle`).
- Manipulação e concatenação de strings.
- Construção de listas e conversão para string com `join()`.
- Formatação de saída com f-strings.

---
Projeto desenvolvido para fins de estudo durante os cursos da **Alura**.