def exerc06():
    print()
    print("6. Contagem de pares e ímpares")
    print("Dada uma lista com 10 números inteiros, conte quantos são pares e quantos são ímpares.")
    print("Exiba as duas quantidades ao final.")

    print()

    numeros = [12, 7, 9, 14, 5, 8, 11, 6, 3, 10]
    pares = 0
    impares = 0

    for numero in numeros:
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1

    print(f"Quantidade de números pares: {pares}")
    print(f"Quantidade de números ímpares: {impares}")


if __name__ == "__main__":
    exerc06()
