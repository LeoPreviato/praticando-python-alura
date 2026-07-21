def contador_vogais(texto):
    contador = 0
    vogais = "aeiou"
    
    for palavra in texto.lower().strip():
        if palavra in vogais:
            contador += 1
            
    return contador
        
texto_usuario = input("Digite um texto: ")

print(f"O texto tem {contador_vogais(texto_usuario)} vogais")
