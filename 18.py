if __name__ == '__main__':
	N1, CD=0.456789, 3
	F="{0:4."+str(CD).strip()+"%}"
	print (F.format(N1))
	print (8*"*")
	CD-=1
	F="{0:4."+str(CD).strip()+"%}"
	print (F.format(N1))
