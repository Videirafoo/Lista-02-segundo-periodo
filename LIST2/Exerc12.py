def exerc12 ():
    
    print()
   
    print("12. Lista sem repetição")
    print("Dada a lista numeros = [2, 5, 2, 8, 5, 9, 2, 8, 10],")
    print("crie uma nova lista contendo cada valor apenas uma vez,")
    print("mantendo a ordem da primeira ocorrência. Não utilize set().")
    
    print()
    
    numeros = [2, 5, 2, 8, 5, 9, 2, 8, 10]
    numeros_sem_repeticao = []
    for n in numeros:
        if n not in numeros_sem_repeticao:
            numeros_sem_repeticao.append(n)
    print("Lista sem repetição:", numeros_sem_repeticao)

if __name__ == "__Main__":
    exerc12()