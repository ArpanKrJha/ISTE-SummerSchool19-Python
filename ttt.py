import tkinter
import random

def printgrid():
    print('\t-------')
    for i in range(1,8,3):
        print('\t'+'|'+grid[i]+'|'+grid[i+1]+'|'+grid[i+2]+'|')
        print('\t-------')

def checkgrid(x):
    if (int(x)>=1 and int(x)<=9) and (grid[int(x)]>='1' and grid[int(x)]<='9'):
        return 1
    else:
        return 0
def checkgridxo(c):
    x='0'
    while x=='0':
        x=input('Player '+c+' Enter grid no. to place '+c+' : ')
        if checkgrid(x)==1:
            grid[int(x)]=c
        else:
            print('Wrong input, please try again')
            x='0'


def check():
    if grid[1]==grid[5]==grid[9]=='X' or grid[3]==grid[5]==grid[7]=='X' or\
    grid[1]==grid[2]==grid[3]=='X' or grid[4]==grid[5]==grid[6]=='X' or\
    grid[7]==grid[8]==grid[9]=='X' or grid[1]==grid[4]==grid[7]=='X' or\
    grid[2]==grid[5]==grid[8]=='X' or grid[3]==grid[6]==grid[9]=='X':
        return 1
    elif grid[1]==grid[5]==grid[9]=='O' or grid[3]==grid[5]==grid[7]=='O' or\
    grid[1]==grid[2]==grid[3]=='O' or grid[4]==grid[5]==grid[6]=='O' or\
    grid[7]==grid[8]==grid[9]=='O' or grid[1]==grid[4]==grid[7]=='O' or\
    grid[2]==grid[5]==grid[8]=='O' or grid[3]==grid[6]==grid[9]=='O':
        return 1
    else:
        return 0


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
        return -1

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

def cpuwins(i,cpuc,player):
    re=0
    if checkgrid(i)==1:
        grid[i]=cpuc
        if check()==1:
            re=1

        else:
            grid[i]=str(i)
    return re

def playerwins(i,cpuc,player):
    re=0
    if checkgrid(i+1)==1:
        grid[i+1]=player
        if check()==1:
            re=1
            grid[i+1]=cpuc

        else:
            grid[i+1]=str(i+1)
    return re

def cpu(cpuc,player):
    re=0
    for i in range(9):
        re=cpuwins(i+1,cpuc,player)
        if re==1:
            break
    else:
        for i in range(9):
            re=playerwins(i+1,cpuc,player)
            if re==1:
                break
        else:
            yes=1
            while yes==1:
                j=random.randrange(1,9,1)
                if checkgrid(j)==1:
                    grid[j]=cpuc
                    break

def pvp():

    win=0
    printgrid()
    while win==0:
        checkgridxo('X')
        win=checktic()
        printgrid()
        if win==1 or win==-1:
            break
        checkgridxo('O')
        win=checktic()
        printgrid()

def pvc():
    win=0
    player='0'
    cpuc='0'
    while player=='0':
        player = input('Which side do you pick? X or O (X starts first): ')
        if player!='X' and player!='x' and player!='O' and player!='o':
            player='0'
        else:
            if player=='X' or player=='x':
                player = 'X'
                cpuc = 'O'
                printgrid()
                win=0
                while win==0:
                    checkgridxo(player)
                    win=checktic()
                    printgrid()
                    if win==1 or win==-1:
                        break
                    print('CPU plays:')
                    cpu(cpuc,player)
                    win=checktic()
                    printgrid()
            else:
                player = 'O'
                cpuc = 'X'
                printgrid()
                win=0
                while win==0:
                    cpu(cpuc,player)
                    win=checktic()
                    printgrid()
                    if win==1 or win==-1:
                        break
                    checkgridxo(player)
                    win=checktic()
                    printgrid()




def play():
    win=0

    pwindow=tkinter.Tk()
    pwindow.title("Tic-Tac-Toe")
    button1 = tkinter.Button(pwindow, text="\t").grid(row=0,column=0)
    button2 = tkinter.Button(pwindow, text="\t").grid(row=0,column=1)
    button3 = tkinter.Button(pwindow, text="\t").grid(row=0,column=2)
    button4 = tkinter.Button(pwindow, text="\t").grid(row=1,column=0)
    button5 = tkinter.Button(pwindow, text="\t").grid(row=1,column=1)
    button6 = tkinter.Button(pwindow, text="\t").grid(row=1,column=2)
    button7 = tkinter.Button(pwindow, text="\t").grid(row=2,column=0)
    button8 = tkinter.Button(pwindow, text="\t").grid(row=2,column=1)
    button9 = tkinter.Button(pwindow, text="\t").grid(row=2,column=2)
    pwindow.mainloop()

grid={1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}
window = tkinter.Tk()
window.title("Tic-Tac-Toe")
tkinter.Label(window, text = "Welcome to Tic-Tac-Toe").pack()
tkinter.Label(window, text = "How would you like to play?").pack()
tkinter.Button(window, text = "1. Player vs Player", command = play).pack()
tkinter.Button(window, text = "2. Player vs CPU", command = play).pack()
window.mainloop()
