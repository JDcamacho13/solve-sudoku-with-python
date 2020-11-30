sudoku = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]


def imprimirSudoku(su):

    for i in range(len(su)):
        if i % 3 == 0:
            print("- - - - - - - - - - - - - - -")

        for j in range(len(su[0])):
            if j % 3 == 0:
                print(" | ", end="")
            if j == 8:
                print(str(su[i][j]) + " | ")

            else:
                print(str(su[i][j]) + " ", end="")
    
    print("- - - - - - - - - - - - - - -")

def encontrarVacio(su):

    for i in range(len(su)):
        for j in range(len(su[0])):
            if su[i][j] == 0:
                return (i,j);
    
    return False

def esValido(su, num, pos):

    # revisamos la fila

    for i in range(len(su[0])):
        if su[pos[0]][i] == num and pos[1] != i:
            return False

    # revisamos la columna

    for i in range(len(su[0])):
        if su[i][pos[1]] == num and pos[0] != i:
            return False

    # revisamos la caja

    cajaX = pos[1] // 3
    cajaY = pos[0] // 3

    for i in range(cajaY * 3, cajaY * 3 + 3):
        for j in range(cajaX * 3, cajaX * 3 +3):
            if su[i][j] == num and (i,j) != pos:
                return False

    return True

def backtracking(su):

    vacio = encontrarVacio(su)
    if not vacio:
        return True
    else:
        fila, columna = vacio

    for i in range(1,10):
        if esValido(su, i, (fila, columna)):
            su[fila][columna] = i;

            if backtracking(su):
                return True
            
            su[fila][columna] = 0

    return False

print("")
imprimirSudoku(sudoku)
print("_____________________________")
backtracking(sudoku)
print("")
imprimirSudoku(sudoku)
