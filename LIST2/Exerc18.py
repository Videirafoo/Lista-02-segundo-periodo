def exerc18():
    print()
    print("18. Frequência dos elementos")
    print("Dada uma lista de números inteiros, informe quantas vezes cada valor aparece.")

    numeros = [2, 3, 2, 5, 3, 2]
    verificados = []

    for numero in numeros:
        if numero not in verificados:
            quantidade = 0
            for valor in numeros:
                if valor == numero:
                    quantidade += 1

            print(numero, "aparece", quantidade, "vez(es)")
            verificados.append(numero)


if __name__ == "__main__":
    exerc18()
