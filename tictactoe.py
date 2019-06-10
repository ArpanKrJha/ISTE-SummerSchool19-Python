
def printgrid():
    print('\t-------')
    for i in range(1,8,3):
        print('\t'+'|'+grid[i]+'|'+grid[i+1]+'|'+grid[i+2]+'|')
        print('\t-------')

def checkgridx():
    x='0'
    while x=='0':
        x=input('Player X, Enter grid no. to place X: ')
        if (int(x)>=1 and int(x)<=9) and (grid[int(x)]>='1' and grid[int(x)]<='9'):
            grid[int(x)]='X'
        else:
            print('Wrong input, please try again')
            x='0'

def checkgrido():
    o='0'
    while o=='0':
        o=input('Player O, Enter grid no. to place O: ')
        if (int(o)>=1 and int(o)<=9) and (grid[int(o)]>='1' and grid[int(o)]<='9'):
            grid[int(o)]='O'
        else:
            print('Wrong input, please try again')
            o='0'

def checktic():
    full=0
    for i in range(9):
        if grid[i+1]>='1' and grid[i+1]<='9':
            full=0
            break
        else:
            full=1

    if full==1:
        print('Game over')
        return 1

    if grid[1]==grid[5]==grid[9]=='X' or grid[3]==grid[5]==grid[7]=='X' or\
    grid[1]==grid[2]==grid[3]=='X' or grid[4]==grid[5]==grid[6]=='X' or\
    grid[7]==grid[8]==grid[9]=='X' or grid[1]==grid[4]==grid[7]=='X' or\
    grid[2]==grid[5]==grid[8]=='X' or grid[3]==grid[6]==grid[9]=='X':
        print('Game Over')
        print('Player X wins')
        return 1

    elif grid[1]==grid[5]==grid[9]=='O' or grid[3]==grid[5]==grid[7]=='O' or\
    grid[1]==grid[2]==grid[3]=='O' or grid[4]==grid[5]==grid[6]=='O' or\
    grid[7]==grid[8]==grid[9]=='O' or grid[1]==grid[4]==grid[7]=='O' or\
    grid[2]==grid[5]==grid[8]=='O' or grid[3]==grid[6]==grid[9]=='O':
        print('Game Over')
        print('Player O wins')
        return 1

    else:
        return 0



grid={1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}
win=0
printgrid()
while win==0:
    checkgridx()
    win=checktic()
    printgrid()
    if win==1:
        break
    checkgrido()
    win=checktic()
    printgrid()
