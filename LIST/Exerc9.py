def exerc09():
    print()
    print("9. Inserção e remoção")
    print("Crie uma lista inicialmente vazia. Leia 5 números e utilize append() para inseri-los.")
    print("Depois, solicite um número ao usuário e remova sua primeira ocorrência, caso exista.")
    print("Exiba a lista antes e depois da remoção.")

    print()

    lista = []
    for _ in range(5):
        numero = int(input("Digite um número: "))
        lista.append(numero)

    print(f"Lista antes da remoção: {lista}")
    numero_remover = int(input("Digite o número a ser removido: "))

    if numero_remover in lista:
        lista.remove(numero_remover)
        print(f"Lista depois da remoção: {lista}")
    else:
        print("Número não encontrado na lista.")


if __name__ == "__main__":
    exerc09()
