#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
	if len(matrix) == 0:
		print("")
	else:
		for ROWitems in matrix:
			for Citems in ROWitems:
				print("{:d}".format(Citems), end=" ")
			print(end="\n")
