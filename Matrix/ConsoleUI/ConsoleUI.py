



matrix = [[1,0,1],[1,1,1],[1,0,0]]
print(type(matrix))
for i in range(len(matrix)):
    for x in range(len(matrix)):
        print(matrix[i][x])
        if matrix[i][x] == 1:
           matrix[i][x] = 2

print(matrix)
