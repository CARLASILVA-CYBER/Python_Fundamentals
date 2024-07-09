if __name__ == '__main__':
	N1 = 4.78905
	F  = "{0:{NC}.{CD}f}"
	print (F.format(N1, NC=5, CD=3))
	print (F.format(N1, NC=4, CD=2))
	print (F.format(N1, NC=1, CD=0))