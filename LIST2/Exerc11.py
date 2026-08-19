def exerc11():
    
    print()
    
    print("11. Fatiamento")
    print("Considere valores = [10, 20, 30, 40, 50, 60, 70, 80].")
    print("Utilizando slicing, exiba: os quatro primeiros elementos;")
    print("os três últimos; os elementos das posições 2 a 5; e a lista invertida.")

    print()
    
    valores = [10, 20, 30, 40, 50, 60, 70, 80]
    print("Quatro primeiros elementos:", valores[:4])
    print("Três últimos elementos:", valores[-3:])
    print("Elementos das posições 2 a 5:", valores[2:6])
    print("Lista invertida:", valores[::-1])
    
if __name__ == "__Main__":
    exerc11()