def square():  # statement make a matrix
    n = int(input())  # input n value to square of matrix
    grid = n ** 2  # grid as limit of the square
    matrix = [[0] * n for i in range(n)]  # make empty list of matrix
    x = 0  # set x as Integer Division of n
    y = 0  # set y is 0
    value = 1  # set start value to 1
    while value <= grid:  # statement filling matrix
        matrix[x][y] = value  # filling value from cordinate
        y += 1  # y cordinate +1 or y = y + 1
        if y > n - 1:  # statement if y bigger than n minus one
            x += 1  # x cordinate +1 or x = x + 1
            y = y - n  # y cordinate minus n
        value += 1  # value incrase one
    rotated(matrix)  # run rotating with matrix value or run print matrix
    rotated(matrix[::-1])  # run rotating with matrix value or run as flip vertically
    rotated(rotate_90(n, rotate_90(n, matrix[::-1])))  # run rotating with matrix value or run as flip horizontally
    rotated(rotate_90(n, matrix))  # run rotating with matrix value or run as rotate 90 degree
    rotated(rotate_90(n, rotate_90(n, matrix)))  # run rotating with matrix value or run as rotate 180 degree
    rotated(rotate_90(n, rotate_90(n, rotate_90(n, matrix))))  # run rotating with matrix value or run as rotate 270 degree
def rotate_90(n, matrix):  # statement make rotate 90 degree
    result = [[0] * n for m in range(n)] #make empty list of new matrix
    for x in range(n): #startting change value with for statement, start with x cordinate
        for y in range(n): #start with y cordinate
            result[y][n - 1 - x] = matrix[x][y] #changing value
    return result #take result value
def rotated(matrix): #statement for rotated matrix
    for row in matrix: #take from row of matrix
        for column in row: #take from colomn of matrix
            print('{0:3d}'.format(column), end=" ") #print out the matrix
        print() #print empty
    print() #making space
square() #run main statement named as square
