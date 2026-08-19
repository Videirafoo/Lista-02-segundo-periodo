def exerc16():
    
    print()
    
    print("16. Lista de listas")
    print("Crie uma matriz 3x3 utilizando listas de listas.")
    print("Exiba todos os elementos, a soma de todos os valores e a soma de cada linha.")
    
    print()
    
    matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    ]

    total = 0

    for linha in matriz:
        soma_linha = 0
        
        for valor in linha:
            print(valor, end=" ")
            total += valor
            soma_linha += valor
        print("- Soma da linha:", soma_linha)

    print("Soma total:", total)

    print()
    
if __name__ == "__main__":
    exerc16()