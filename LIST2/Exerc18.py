def exerc18():
    
    print()
    
    print("18. Frequência dos elementos")
    print("Dada uma lista de números inteiros, informe quantas vezes")
    print("cada valor aparece. Exemplo: para [2, 3, 2, 5, 3, 2],")  
    print("a saída deve indicar que 2 aparece 3 vezes, 3 aparece 2 vezes e 5 aparece 1 vez.")
    
    print()
    
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

    print()
      
if __name__ == "__main__":
    exerc18()