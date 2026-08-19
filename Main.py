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

Exercicios = [
Exerc1,
Exerc2,
Exerc3,
Exerc4,
Exerc5,
Exerc6,
Exerc7,
Exerc8,
Exerc9,
Exerc10,
Exerc11,
Exerc12,
Exerc13,
Exerc14,
Exerc15,
Exerc16,
Exerc17,
Exerc18,
Exerc19,
Exerc20
]

print()
print("Lista de Exercícios de LP")
print("Escolha um exercício para executar:")

print()
for numero, exercicio in enumerate(Exercicios, start=1):

    exercicio()

    if numero < len(Exercicios):

        input(f"Pressione Enter para continuar para o próximo exercício ({numero + 1})...")

        print("\n" + "-" * 50 + "\n")