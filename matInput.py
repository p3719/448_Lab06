def getMatrixFromCSV(fileName = 'matrixA.csv'):
    file = open(fileName)

    rowsSize = []
    csvFormat = True
    matrix = []
    for line in file:
        buffer = line.replace(" ", '').replace("\n", '')
        if buffer:
            buffer = list(buffer.split(','))
            auxBuffer = []
            for num in buffer:
                auxBuffer.append(float(num))
            buffer = auxBuffer
            if not rowsSize:
                rowsSize = len(buffer)
            if rowsSize != len(buffer):
                csvFormat = False
                break
            else:
                matrix.append(buffer)
    else:
        return matrix
