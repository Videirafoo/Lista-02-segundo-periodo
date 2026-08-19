def exerc07():
    print()

    print("7. Busca de um elemento ")
    print("Leia 8 números e armazene-os em uma lista.") 
    print("Depois, solicite ao usuário um número para pesquisar.")
    print("Informe se ele está ou não na lista. Não utilize index() para realizar a busca.")
    
    print()

    numeros = []
    for i in range(8):
        numero = int(input(f"Digite o {i + 1}º número: "))
        numeros.append(numero)
        
    numero_pesquisado = int(input("Digite o número a ser pesquisado: "))
    encontrado = False
    for n in numeros:
        if n == numero_pesquisado:
            encontrado = True
            break

    if encontrado:
        print(f"O número {numero_pesquisado} está na lista.")
    else:
        print(f"O número {numero_pesquisado} não está na lista.")

if __name__ == "__Main__":
    exerc07()