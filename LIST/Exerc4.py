def exerc04():
    print()
    print("4. Média de uma lista")
    print("Considere notas = [7.5, 8.0, 6.0, 9.5, 5.5].")
    print("Calcule a média manualmente, percorrendo a lista. Ao final,")
    print("informe a média com duas casas decimais.")

    print()

    notas = [7.5, 8.0, 6.0, 9.5, 5.5]
    soma = 0

    for nota in notas:
        soma += nota

    media = soma / len(notas)
    print(f"A média das notas é: {media:.2f}")


if __name__ == "__main__":
    exerc04()
