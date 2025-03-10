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



#Task 05: Game Arena

def play_game(arena):
  row=len(arena)
  col=len(arena[0])
  point = 0
  for i in range(row):
    for j in range(col):
      if arena[i][j]>=50 and arena[i][j]%50 == 0:
        if i > 0 and arena[i-1][j] == 2:
          point += 2
        if i < row-1 and arena[i+1][j] == 2:
          point += 2
        if j > 0 and arena[i][j-1] == 2:
          point += 2
        if j < col-1 and arena[i][j+1] == 2:
          point += 2

  if point >= 10:
    print(f"Points Gained: {point}. Your team has survived the game.")
  else:
    print(f"Points Gained: {point}. Your team is out.")



#DO NOT CHANGE THE CODE BELOW
arena=np.array([[0,2,2,0],
                [50,1,2,0],
                [2,2,2,0],
                [1,100,2,0]
                ])
print_matrix(arena)
play_game(arena)
#This should print
#Points Gained: 6. Your team is out.
print(".....................")
arena=np.array([[0,2,2,0,2],
                [1,50,2,1,100],
                [2,2,2,0,2],
                [0,200,2,0,0]
                ])
print_matrix(arena)
play_game(arena)
#This should print
#Points Gained: 14. Your team has survived the game.