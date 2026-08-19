def exerc15():
    
    print()
    
    print("15. Listas paralelas")
    print("Crie duas listas: uma com 5 nomes de alunos e outra com suas respectivas notas.")
    print("Percorra as listas simultaneamente e exiba o nome, a nota e a situação de cada aluno,")
    print("considerando aprovação com nota maior ou igual a 6.")
    
    print()
    
    nomes = ["Alice", "Bob", "Charlie", "David", "Eve"]
    notas = [7.5, 5.0, 8.0, 6.5, 4.0]
    
    for i in range(5):
        print(f"Aluno: {nomes[i]}, Nota: {notas[i]}")
        if notas[i] >= 6.0:
            print("Situação: Aprovado")
        else:
            print("Situação: Reprovado")
    
    
    print()

if __name__ == "__main__":
    exerc15()