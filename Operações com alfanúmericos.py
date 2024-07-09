if __name__ == '__main__':
	E1, E2 =len("Alcochete"), "Almada" 							#DETERMINA O COMPRIMENTO DA STRING ALCOCHETE
	E3, E4 = " fica em Setúbal", "Coimbra".upper()				#CONCATENANDO A STRING E CONVERTENDO "COIMBRA" PARA MAIUSCULAS
	E5 ="Carla Sofia Silva" [6:11]								#EXTRAINDO A SUBCADEIA
	E6, E7, E8 = "ABCCD", "ABBCD", "ABCCD"						#DEFENINDO AS STRINGS
	E9, E10 = "Ricardo Ribeiro Seixal", "Boa Noite".strip(" ")	#REMOVENDO ESPAÇOS À DIREITA E À ESQUERDA DA STRING "BOA NOITE"

	print (E1)
	print (E2+E3)
	print (E4)
	print (E5)
	print (E6==E7)
	print (E7<E8)
	print (E9.find("Seixal", 1, len(E9)))
	print (E10)
