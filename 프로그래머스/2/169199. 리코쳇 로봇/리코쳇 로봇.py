from collections import deque

def makeVisited(rowlen, collen):
    visited = []
    for _ in range(rowlen):
        visited.append([-1] * collen)
    return visited
    

def findR(board, rowlen, collen):
    for i in range(rowlen):
        for j in range(collen):
            if(board[i][j] == "R"):
                return [i, j]
    return [-1, -1]

def slide(board, row, col, dRow, dCol):
    while(True):
        if(row >= len(board) or col >= len(board[0]) or row < 0 or col < 0 or board[row][col] == "D"):
            return [row - dRow , col - dCol]
        row += dRow
        col += dCol
    

def solution(board):
    rowlen = len(board)
    collen = len(board[0])
    
    visited = makeVisited(rowlen, collen)
    
    row, col = findR(board, rowlen, collen)
    que = deque()
    que.append([row, col])
    visited[row][col] = 0
    
    d = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    
    while(len(que) > 0):
        row, col = que.popleft()
        if(board[row][col] == "G"):
            return visited[row][col]
        
        for i in range(4):
            dRow, dCol = d[i]
            i, j = slide(board, row, col, dRow, dCol )
            if(visited[i][j] == -1): 
                que.append([i, j])
                visited[i][j] = visited[row][col] + 1
        
    return -1