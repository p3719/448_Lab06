import matInput
import matMult
import matTrans
import matOutput
import matCheck

def main():

    # Get matrices
    matrixA = matInput.getMatrixFromCSV('matrixA.csv')
    if not matCheck.CheckMatrix(matrixA):
    	print("MatrixA is not a matrix!")
    matrixB = matInput.getMatrixFromCSV('matrixB.csv')
    if not matCheck.CheckMatrix(matrixA):
    	print("MatrixB is not a matrix!")
    
    
    exit = False
    while(not exit):
        exit = menu(matrixA, matrixB)
        
    

def menu(matrixA = [], matrixB = []):
    # Ask operation
    print("\n\n")
    print("==================\n")
    print("Matrix Operations\n")
    print("==================\n")
    print("1 - Multiplication\n")
    print("2 - Addition\n")
    print("3 - Transpose\n")
    print("4 - Exit\n")
    operation = int(input('Your option: '))

    # Get matrices
    if not matrixA:
        matrixA = matInput.getMatrixFromCSV('matrixA.csv')
    if not matrixB:
        matrixB = matInput.getMatrixFromCSV('matrixB.csv')
    
    if operation != 4:
        matOutput.showMatrix(matrixA, 'A')
        matOutput.showMatrix(matrixB, 'B')
        
    # Choose the operation
    if operation == 1:
        if matrixA and matrixB:
            result = matMult.multiplication(matrixA, matrixB)
            if not result:
                print("\n\nMatrices cannot be multiplied.\n\n")
            else:
                matOutput.showMatrix(result, 'Result')
        else:
            print("\n\nMatrices were not found.\n\n")
    elif operation == 2:
        if matrixA and matrixB:
            result = []
        #    result = matAdd.addition(matrixA, matrixB)
            if not result:
                print("\n\nMatrices cannot be summed.\n\n")
            else:
                matOutput.showMatrix(result, 'Result')
        else:
            print("\n\nMatrices were not found.\n\n")
    elif operation == 3:
        if matrixA:
            resultA = matTrans.transpose(matrixA)
            matOutput.showMatrix(resultA, 'ResultA')
            resultB = matTrans.transpose(matrixB)
            matOutput.showMatrix(resultB, 'ResultB')
            
        else:
            print("\n\nMatrix was not found.\n\n")
    elif operation == 4:
        return True
    else:
        print("\n\nInvalid operation.\n\n")
    return False
    
main()
