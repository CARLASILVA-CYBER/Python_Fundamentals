from datetime import datetime

if __name__ == '__main__':
	I=int(5.76)
	R=float(4)
	S=str(4.567)
	A=float("234.6")
	D=datetime.strptime("23/03/2024", "%d/%m/%Y").date()

	print(f"{I} \t{R} \t{S}\t{A}")

	print(f"{D:%d/%m/%Y}")
