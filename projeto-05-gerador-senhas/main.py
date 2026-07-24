import random

def gerar_senha():
    l_maiusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    l_minusculas = "abcdefghijklmnopqrstuvwxyz"
    numeros = "123456789"
    c_especiais = "!@#$%&*_"
    
    senha = [
        random.choice(l_maiusculas),
        random.choice(l_minusculas),
        random.choice(numeros),
        random.choice(c_especiais)
    ]
    
    todos_caracteres = l_maiusculas + l_minusculas + numeros + c_especiais
    
    senha.extend(random.choices(todos_caracteres, k=8))
    random.shuffle(senha)
    return ''.join(senha)

print(f"Senha gerada: {gerar_senha()}")
