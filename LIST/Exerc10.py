def exerc10():
    print()
    print("10. Ordenação")
    print("Considere numeros = [18, 5, 12, 3, 20, 7, 9].")
    print("Exiba a lista original, depois a lista em ordem crescente")
    print("e finalmente em ordem decrescente. Utilize sort() ou sorted().")

    print()

    numeros = [18, 5, 12, 3, 20, 7, 9]
    print("Lista original:", numeros)

    # sort() altera a própria lista. sorted() cria e retorna uma nova lista ordenada.
    numeros.sort()
    print("Lista em ordem crescente:", numeros)

    numeros.sort(reverse=True)
    print("Lista em ordem decrescente:", numeros)


if __name__ == "__main__":
    exerc10()
