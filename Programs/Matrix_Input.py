# 2D Matrix Input

def take_input(data):
    try:
        data = int(data)
    except:
        data = -1
    return data
    

row = take_input(input('Enter the row: '))
column = take_input(input('Enter the column: '))

# Taking matrix input
at = 0
matrix = []
for i in range(row):
    mtx1 = []
    for j in range(column):
        at = input()
        mtx1.append(take_input(at))
    matrix.append(mtx1)

print('Matrix Row- {} and Cloumn- {}'.format(row, column))
if row == -1 and column == -1:
    print('Program is quitting for Unvalid values')
    exit()

# Printing the matrix
for i in range(row):
    for j in range(column):
        print(matrix[i][j], end=' ')
    print()
