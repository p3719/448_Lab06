def multiplication(matrixA, matrixB):
    matrixC = []
    if checkMultiplicationSize(matrixA, matrixB):
        for i in range(len(matrixA)):
            matrixC.append([])
            for j in range(len(matrixB[0])):
                matrixC[i].append(0)
                
        for row in range(len(matrixA)):
            for column in range(len(matrixB[0])):
                matrixC[row][column] = 0
                for common in range(len(matrixB)):
                    matrixC[row][column] += matrixA[row][common] * matrixB[common][column]
    return matrixC

def checkMultiplicationSize(matrixA, matrixB):
    return len(matrixA[0]) == len(matrixB)
