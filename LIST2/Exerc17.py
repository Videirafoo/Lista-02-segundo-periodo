def exerc17():
    print()
    print("17. Segundo maior valor")
    print("Dada uma lista de números inteiros, encontre o segundo")
    print("maior valor distinto sem utilizar sort(). Considere que a lista")
    print("possui pelo menos dois valores distintos.")

    print()

    numeros = [10, 5, 20, 8, 20, 15]
    maior = None
    segundo = None

    for numero in numeros:
        if maior is None or numero > maior:
            if numero != maior:
                segundo = maior
                maior = numero
        elif numero != maior and (segundo is None or numero > segundo):
            segundo = numero

    print("Segundo maior:", segundo)
    print()


if __name__ == "__main__":
    exerc17()
