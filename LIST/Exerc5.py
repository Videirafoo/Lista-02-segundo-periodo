def exerc05():
   
    print()
    print("5. Maior e menor valor.")
    print("Crie uma lista de números inteiros e determine o maior e o menor elemento sem utilizar max() ou min().")
    
    print()
    numeros = [15, 22, 8, 19, 31, 5, 12]
    maior = numeros[0]
    menor = numeros[0]
    for numero in numeros:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    print(f"O maior valor da lista é: {maior}")
    print(f"O menor valor da lista é: {menor}")
if __name__ == "__Main__":
    exerc05()