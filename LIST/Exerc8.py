def exerc08():
   
    print()

    print("8. Posição de um elemento")  
    print("Considere nomes = ['Ana', 'Bruno', 'Carlos', 'Daniel', 'Eduarda'].")
    print(" Solicite um nome ao usuário e")
    print("informe a posição em que ele aparece. Caso não exista, informe que o nome não foi encontrado.")
    
    print()

    nomes = ["Ana", "Bruno", "Carlos", "Daniel", "Eduarda"]
    nome_pesquisado = input("Digite um nome para pesquisar: ")
    posicao = -1
    for i, nome in enumerate(nomes):
        if nome == nome_pesquisado:
            posicao = i
            break
    if posicao != -1:
        print(f"O nome {nome_pesquisado} está na posição {posicao}.")
    else:
        print(f"O nome {nome_pesquisado} não foi encontrado.")

if __name__ == "__Main__":
    exerc08()