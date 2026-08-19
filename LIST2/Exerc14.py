def exerc14():
    
    print()
    
    print("14. Compreensão de listas")
    print("Considere numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].")
    print("Crie, utilizando compreensão de listas: uma lista com os quadrados;")
    print("uma lista somente com os pares; e uma lista contendo apenas os números maiores que 5.")
    
    print()
    
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    quadrados = [n**2 for n in numeros]
    pares = [n for n in numeros if n % 2 == 0]
    maiores_que_cinco = [n for n in numeros if n > 5]
    
    print("Quadrados:", quadrados)
    print("Pares:", pares)
    print("Maiores que 5:", maiores_que_cinco)

    print()
    
if __name__ == "__main__":
    exerc14()