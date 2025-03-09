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



def row_rotation(exam_week, seat_status):
    row=len(seat_status)
    col=len(seat_status[0])

    for i in range(exam_week):
      last = np.zeros(col, dtype=seat_status.dtype)
      for j in range(col):
        last[j] = seat_status[row - 1][j]

      for i in range(row - 1, 0, -1):
        seat_status[i] = seat_status[i - 1]
      seat_status[0] = last

    for i in range(row):
        for j in range(col):
            if seat_status[i][j] == "AA":
                return i


#DO NOT CHANGE THE CODE BELOW
seat_status = np.array([[ 'A' , 'B' , 'C' , 'D' , 'E'],
                  ['F' , 'G' , 'H' , 'I' , 'J'],
                  ['K' , 'L' , 'M' , 'N' , 'O'],
                  ['P' , 'Q' , 'R' , 'S' , 'T'],
                  ['U' , 'V' , 'W' , 'X' , 'Y'],
                  ['Z' , 'AA' , 'BB' , 'CC' , 'DD']])
exam_week=3
print_matrix(seat_status)
print()

row_number=row_rotation(exam_week, seat_status) #This should print modified seat status after rotation and return the row number
print(f'Your friend AA will be on row {row_number}') #This should print Your friend AA will be on row 2