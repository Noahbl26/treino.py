print("conador de letras A em uma frase")
frase=input("digite uma frase:")
contador=0

for letra in frase:
    if letra.lower() == "a":
        contador += 1
print(f"o total de letras 'a':{contador}")
