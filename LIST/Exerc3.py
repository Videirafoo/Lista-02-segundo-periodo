def exerc03():
    print()
    print("3. Soma dos elementos")
    print("Crie uma lista com 8 números inteiros.")
    print("Calcule e exiba a soma de todos os elementos")
    print("sem utilizar a função sum().")

    print()

    numeros = [1, 2, 3, 4, 5, 6, 7, 8]
    soma = 0

    for numero in numeros:
        soma += numero

    print(f"A soma dos elementos é: {soma}")


if __name__ == "__main__":
    exerc03()
