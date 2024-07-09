# _*_coding: UTF-8 -*
from enum import Enum

if __name__ == '__main__':
	Notas= Enum("Notas", "E,D,C,B,A")

	print(Notas.A.value, "- Distinção: ", Notas.A.name)
	print(Notas.B.value, Notas.C.value, " - Aprovados: ", Notas.B.name, Notas.C.name)
	print(Notas.D.value, Notas.E.value, " - Prova Oral: ", Notas.D.name, Notas.E.name)
