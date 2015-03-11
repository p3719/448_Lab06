def showMatrix(matrix, label = ''):
    print("\n\n")
    if label:
        print(label, " = ")
    for row in range(len(matrix)):
        print("\n[ ", sep="", end="")
        for column in range(len(matrix[0])):
            print(matrix[row][column], " ", sep="", end="")
        print("]", sep="", end="")
