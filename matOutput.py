import sys

def showMatrix(matrix, label = ''):
    print("\n\n")
    if label:
        print(label, " = ")
    for row in range(len(matrix)):
        printf("\n[ ")
        for column in range(len(matrix[0])):
            printf(str(matrix[row][column]))
            printf(" ")
        printf("]")

def printf(message):
	 sys.stdout.write(message)
	