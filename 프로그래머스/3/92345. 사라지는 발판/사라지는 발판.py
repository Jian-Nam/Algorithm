import sys
def recursion(board, aloc, bloc, tcount):
    turn = tcount % 2
    notturn = 1 if turn == 0 else 0
    # print(turn, notturn)
    if(board[aloc[0]][aloc[1]] == 0):
        return [1, tcount]
    if(board[bloc[0]][bloc[1]] == 0):
        return [0, tcount]
    direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    
    mywin = []
    youwin = []
    for di, dj in direction:
        i, j = aloc if turn == 0 else bloc
        ni, nj = i + di, j + dj
        if(ni < len(board) and ni >= 0 and nj < len(board[0]) and nj >= 0 and board[ni][nj] == 1):
            naloc = [ni, nj] if turn == 0 else aloc
            nbloc = [ni, nj] if turn == 1 else bloc
            nboard = [arr[:] for arr in board]
            nboard[i][j] = 0
            nwinner, nturncount = recursion(nboard, naloc, nbloc, tcount + 1)
            
            if(nwinner == turn):
                mywin.append(nturncount)
            else:
                youwin.append(nturncount)
    # print(turn, mywin, youwin)
    if(len(mywin) > 0):
        return [turn, min(mywin)]
    if(len(youwin) > 0):
        return [notturn, max(youwin)]

    return [notturn, tcount] # 우승자, 턴수

def solution(board, aloc, bloc):
    print(recursion(board, aloc, bloc, 0))
    return recursion(board, aloc, bloc, 0)[1]