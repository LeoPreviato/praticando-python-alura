def identificador_palavras(texto):
    texto_formatado = texto.split()
    lista_palavras = []
    
    for palavra in texto_formatado:
        if len(palavra) > 10:
            lista_palavras.append(palavra)
    if len(lista_palavras) == 0:
        return "Nenhuma palavra longa foi encontrada no texto"
    else:
        return f"Palavras longas encontradas: {', '.join(lista_palavras)}"

texto_usuario = input("Digite um texto: ").strip()

resultado = identificador_palavras(texto_usuario)

print(resultado)
