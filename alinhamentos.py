if __name__== "__main__":
	E1, E2=20, 50
	nome1, nome2, nome3="Carla Silva", "Joana Carreteiro", "Teresa Gomes"
	local1, local2, local3="Alcochete", "Almada", "Porto"

	print (f"{nome1:<{E1}} {local1:<{E2}}")
	print (f"{nome2:^{E1}} {local2:<{E2}}")
	print (f"{nome3} \t {local3} \n")
