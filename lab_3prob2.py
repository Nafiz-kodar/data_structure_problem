import numpy as np

#DO NOT CHANGE THE CODE BELOW
#You must run this cell to print matrix and for the driver code to work
def print_matrix(m):
  row,col = m.shape
  for i in range(row):
    c = 1
    print('|', end='')
    for j in range(col):
      c += 1
      if(len(str(m[i][j])) == 1):
        print(' ',m[i][j], end = '  |')
        c += 6
      else:
        print(' ',m[i][j], end = ' |')
        c += 6
    print()
    print('-'*(c-col))


#Task 02: Decryption Process

def decrypt_matrix(matrix):
    row=len(matrix)
    col=len(matrix[0])
    arr=np.zeros((row,col), dtype=int)
    for i in range(col):
      sum=0
      for j in range(row):
        sum+=matrix[j][i]
        arr[j][i]=sum

    arr2=np.zeros((1,col-1),dtype=int)
    for i in range(col-1):
        n=arr[row-1][i+1]-arr[row-1][i]
        arr2[0][i]=n
    return arr2

#DO NOT CHANGE THE CODE BELOW
matrix=np.array([[1,3,1],
                 [6,4,2],
                 [5,1,7],
                 [9,3,3],
                 [8,5,4]
                 ])

returned_array=decrypt_matrix(matrix)
print(returned_array)
#This should print [-13, 1]