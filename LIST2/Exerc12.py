def exerc12():
    print()
    print("12. Lista sem repetição")
    print("Dada a lista numeros = [2, 5, 2, 8, 5, 9, 2, 8, 10],")
    print("crie uma nova lista contendo cada valor apenas uma vez,")
    print("mantendo a ordem da primeira ocorrência. Não utilize set().")

    print()

    numeros = [2, 5, 2, 8, 5, 9, 2, 8, 10]
    numeros_sem_repeticao = []

    for numero in numeros:
        if numero not in numeros_sem_repeticao:
            numeros_sem_repeticao.append(numero)

    print("Lista sem repetição:", numeros_sem_repeticao)


if __name__ == "__main__":
    exerc12()
