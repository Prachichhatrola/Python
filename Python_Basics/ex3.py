picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

for x in picture:
    for y in x:
        if y == 0:
            print(' ',end='')
        else:
            print('*',end='')
    print('\n', end='')
