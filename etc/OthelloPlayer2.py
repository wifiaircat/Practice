from threading import Thread
import time
from socket import *

dirs = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
def Changable(i, j, di, dj, stone, board):
    n = 1
    flag = False
    while 8 > i + di*n >= 0 and 8 > j + dj*n >= 0:
        if board[i + di*n][j + dj*n] == stone:
            return True
        if board[i + di*n][j + dj*n] == ' ':
            return False
        n += 1
    return flag

def GetPosition(stone, board):
    # how aboout make proioty location lists
    pro1 = ("0,0", "0,7", "7,0", "7,7")
    pro2 = ("2,2", "5,2", "2,5", "5,5")
    pro3 = ("0,2", "2,0", "5,0", "7,2", "0,5", "2,7", "5,7", "7,5")
    pro4 = ("3,0", "4,0", "3,7", "4,7", "7,3", "7,4", "0,3", "0,4")
    loc = []    
    for i in range(8):
        for j in range(8):
            if board[i][j] in 'WB':
                continue
            # if ocuppied, next
            for d in dirs:
                di = d[0]
                dj = d[1]
            # check around blocks(8)
                if stone == 'B':
                    enemy = 'W'
                else:
                    enemy = 'B'
                if 8 > i + di >= 0 and 8 > j + dj >= 0 and board[i + di][j + dj] == enemy and Changable(i, j, di, dj, stone, board):
                    loc += [str(i)+","+str(j)]
    #break
    for k in loc:
        if k in pro1:
            return loc

    for k in loc:
        if k in pro2:
            return loc
        
    for k in loc:
        if k in pro3:
            return loc
        
    for k in loc:
        if k in pro4:
            return loc
    
    return "-1,-1"

if __name__ == "__main__":
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect(('127.0.0.1', 10000))
    while True:
        #time.sleep(1)
        sb = sock.recv(1000)
        #print(sb)
        board = eval(sb)
        for line in board:
            print(line)
        #val = input("input i, j : ")
        val = GetPosition('W', board)
        print(val)
        sock.send(val.encode())
        #break
