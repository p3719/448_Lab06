def transpose(matrixA):
    matrixB = []
    numRows = len(matrixA)
    numColumns = len(matrixA[0])
    for row in range(numColumns):
        matrixB.append([])
        for column in range(numRows):
            matrixB[row].append(0)
            matrixB[row][column] = matrixA[column][row]    
    return matrixB
