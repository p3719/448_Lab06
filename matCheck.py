def CheckMatrix(matrix):
	for x in range(len(matrix)):
		if x == 0:
			cols = len(matrix[x])
		else:
			if len(matrix[x]) != cols:
				return False
	return True