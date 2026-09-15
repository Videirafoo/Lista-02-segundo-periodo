from LIST.Exerc1 import exerc01
from LIST.Exerc2 import exerc02
from LIST.Exerc3 import exerc03
from LIST.Exerc4 import exerc04
from LIST.Exerc5 import exerc05
from LIST.Exerc6 import exerc06
from LIST.Exerc7 import exerc07
from LIST.Exerc8 import exerc08
from LIST.Exerc9 import exerc09
from LIST.Exerc10 import exerc10
from LIST2.Exerc11 import exerc11
from LIST2.Exerc12 import exerc12
from LIST2.Exerc13 import exerc13
from LIST2.Exerc14 import exerc14
from LIST2.Exerc15 import exerc15
from LIST2.Exerc16 import exerc16
from LIST2.Exerc17 import exerc17
from LIST2.Exerc18 import exerc18
from LIST2.Exerc19 import exerc19
from LIST2.Exerc20 import exerc20

exercicios = [
    exerc01,
    exerc02,
    exerc03,
    exerc04,
    exerc05,
    exerc06,
    exerc07,
    exerc08,
    exerc09,
    exerc10,
    exerc11,
    exerc12,
    exerc13,
    exerc14,
    exerc15,
    exerc16,
    exerc17,
    exerc18,
    exerc19,
    exerc20,
]


def main():
    print("Lista de Exercícios de LP")
    print("Os exercícios serão executados em sequência.")

    for numero, exercicio in enumerate(exercicios, start=1):
        exercicio()

        if numero < len(exercicios):
            input(
                f"Pressione Enter para continuar para o próximo exercício "
                f"({numero + 1})..."
            )
            print("\n" + "-" * 50 + "\n")


if __name__ == "__main__":
    main()
