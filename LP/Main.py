from Exerc1 import exerc01 
from Exerc2 import exerc02
from Exerc3 import exerc03
from Exerc4 import exerc04
from Exerc5 import exerc05
from Exerc6 import exerc06
from Exerc7 import exerc07
from Exerc8 import exerc08
from Exerc9 import exerc09
from Exerc10 import exerc10
from Exerc11 import exerc11
from Exerc12 import exerc12
from Exerc13 import exerc13
from Exerc14 import exerc14
from Exerc15 import exerc15
from Exerc16 import exerc16
from Exerc17 import exerc17
from Exerc18 import exerc18
from Exerc19 import exerc19
from Exerc20 import exerc20

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