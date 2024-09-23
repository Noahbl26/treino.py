def fatorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

# Solicitar ao usuário um número
numero = int(input("Digite um número para calcular o fatorial: "))
fatorial_num = fatorial(numero)
print(f"O fatorial de {numero} é: {fatorial_num}")

#A função fatorial(n) inicializa uma variável resultado com 1.
#Em seguida, utiliza um loop for para multiplicar resultado por todos os números de 1 até n.
#Por fim, o resultado é retornado e exibido ao usuário
