import numpy as np

#DO NOT CHANGE THE CODE BELOW
#You must run this cell to print matrix and for the driver code to work
def print_matrix(m):
  num_rows, num_cols = m.shape
  for i in range(num_rows):
    c = 1
    print('|', end='')
    for j in range(num_cols):
      c += 1
      if(len(str(m[i][j])) == 1):
        print(' ',m[i][j], end = '  |')
        c += 6
      else:
        print(' ',m[i][j], end = ' |')
        c += 6
    print()
    print('-'*(c-num_cols))


#Task 04: Matrix Compression
def compress_matrix(mat):
  row=len(mat)
  col=len(mat[0])
  n_matrix = np.zeros((row//2,col//2), dtype=int)

  for j in range(0,col-1,2):
    for i in range(0,row-1):
      if i %2==0:
        sum = mat[i][j] + mat[i+1][j] + mat[i][j+1] + mat[i+1][j+1]
        n_matrix[i//2][j//2] = sum

      else:
        continue
  return n_matrix

#DO NOT CHANGE THE CODE BELOW
matrix=np.array([[1,2,3,4],
                 [5,6,7,8],
                 [1,3,5,2],
                 [-2,0,6,-3]
                 ])
print_matrix(matrix)
print("...............")
returned_array=compress_matrix(matrix)
print_matrix(returned_array)
#This should print

#|  14  |  22 |
#--------------
#|  2  |  10  |
#--------------