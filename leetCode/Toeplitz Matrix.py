matrix =  [
  [1,2,3,4],
  [5,1,2,3],
  [9,5,1,2]
]

for i in range(0,len(matrix)-1):
    for j in range(0,len(matrix[i])-1):
        if matrix[i][j] != matrix[i+1][j+1]:
                print("False")
print("True")