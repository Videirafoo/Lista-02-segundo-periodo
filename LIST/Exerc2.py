def exerc02():
    print()
    print("2. Percorrendo uma lista")
    print("Considere a lista numeros = [7, 12, 5, 18, 3, 20].")
    print("Percorra a lista e exiba cada elemento em uma linha.")
    print("Depois, exiba somente os valores maiores que 10.")

    print()

    numeros = [7, 12, 5, 18, 3, 20]

    for numero in numeros:
        print(numero)

    print("Valores maiores que 10:")
    for numero in numeros:
        if numero > 10:
            print(numero)


if __name__ == "__main__":
    exerc02()
