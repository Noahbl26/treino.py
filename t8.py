def contagem_caracteres(texto):
    contagem = {}
    
    for caractere in texto:
        if caractere in contagem:
            contagem[caractere] += 1
        else:
            contagem[caractere] = 1
    
    return contagem

# Solicitar ao usuário uma string
entrada = input("Digite uma string: ")
resultado = contagem_caracteres(entrada)

# Exibir o resultado
for caractere, quantidade in resultado.items():
    print(f"'{caractere}': {quantidade} vezes")
