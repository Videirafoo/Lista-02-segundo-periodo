def exerc13 ():
    
    print()
    
    print("13. Valores acima da média")
    print("Leia 10 números reais e armazene-os em uma lista.") 
    print("Calcule a média e depois exiba somente os valores que ficaram acima da média.")
          
    print()
    
    numeros = []
    total = 0

    for i in range(10):
        numero = float(input("Digite um número: "))
        numeros.append(numero)
        total += numero

    media = total / len(numeros)
    print("Média:", media)
    print("Acima da média:")

    for numero in numeros:
        if numero > media:
            print(numero)
    print()

if __name__ == "__Main__":
    exerc13()