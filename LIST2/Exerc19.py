def exerc19():
    
    print()
    
    print("19. Problema real — Controle de estoque")
    print('Uma pequena loja possui os produtos ["Teclado", "Mouse", "Monitor", "Notebook", "Headset"]')
    print("e as respectivas quantidades [12, 25, 4, 3, 8]. Desenvolva um programa que permita consultar")
    print("um produto, alterar sua quantidade e listar os produtos com estoque inferior a 5 unidades.")
    print("Ao final, informe qual produto possui a maior quantidade em estoque.")
    
    print()
    
    produtos = ["Teclado", "Mouse", "Monitor", "Notebook", "Headset"]
    quantidades = [12, 25, 4, 3, 8]

    busca = input("Produto para consultar: ")
    posicao = -1

    for i in range(len(produtos)):
        if produtos[i] == busca:
            posicao = i
            break

    if posicao != -1:
        print("Quantidade atual:", quantidades[posicao])
        nova = int(input("Nova quantidade: "))
        quantidades[posicao] = nova
    else:
        print("Produto não encontrado.")

    print("Estoque inferior a 5:")
    for i in range(len(produtos)):
        if quantidades[i] < 5:
            print(produtos[i], "-", quantidades[i])

    maior_posicao = 0
    for i in range(1, len(quantidades)):
        if quantidades[i] > quantidades[maior_posicao]:
            maior_posicao = i

    print("Maior estoque:", produtos[maior_posicao], "-", quantidades[maior_posicao])

    print()
    
if __name__ == "__main__":
    exerc19()   