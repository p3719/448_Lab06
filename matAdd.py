def addition(matrixA, matrixB):
	matrixC = []
	#  If the matrixes can be added then they are
	if CheckAdditionSize(matrixA, matrixB):
		for rows in range(len(matrixA)):
			matrixC.append([])
			for cols in range(len(matrixA[0])):
				matrixC[rows].append(matrixA[rows][cols] + matrixB[rows][cols])
	return matrixC
		
def CheckAdditionSize(matrixA, matrixB):
	#  If the matrixes are of the same size return true otherwise false
	if len(matrixA) == len(matrixB) and len(matrixA[0]) == len(matrixB[0]):
		return True
	return False