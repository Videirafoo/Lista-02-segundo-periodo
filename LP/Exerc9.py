def exerc09():
    print()

    print("9. Inserção e remoção")  
    print("Crie uma lista inicialmente vazia. Leia 5 números e utilize append() para inseri-los.")
    print("Depois, solicite um número ao usuário e remova sua primeira ocorrência, caso exista. Exiba a lista antes e depois da remoção.")

    print()
    lista = []
    for _ in range(5):
        num = int(input("Digite um número: "))
        lista.append(num)
    print(f"Lista antes da remoção: {lista}")
    num_remover = int(input("Digite o número a ser removido: "))
    if num_remover in lista:
        lista.remove(num_remover)
        print(f"Lista depois da remoção: {lista}")
    else:
        print("Número não encontrado na lista.")

if __name__ == "__main__":
    exerc09()