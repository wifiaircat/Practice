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

    for i in range(8):
        for j in range(8):
            if board[i][j] in 'WB':
                continue
            for d in dirs:
                di = d[0]
                dj = d[1]
                if stone == 'B':
                    enemy = 'W'
                else:
                    enemy = 'B'
                if 8 > i + di >= 0 and 8 > j + dj >= 0 and board[i + di][j + dj] == enemy and Changable(i, j, di, dj, stone, board):
                    
                    loc += [str(i)+","+str(j)]
                    return loc
                    #break
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
