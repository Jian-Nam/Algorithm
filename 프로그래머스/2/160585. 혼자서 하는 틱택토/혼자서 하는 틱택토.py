import copy

def isEnd(side, board):
    resultSheet = [1]*8
    for i in range(3):
        resultSheet[0] *= (board[0][i] == side)
        resultSheet[1] *= (board[1][i] == side)
        resultSheet[2] *= (board[2][i] == side)
        resultSheet[3] *= (board[i][0] == side)
        resultSheet[4] *= (board[i][1] == side)
        resultSheet[5] *= (board[i][2] == side)
        resultSheet[6] *= (board[i][i] == side)
        resultSheet[7] *= (board[i][2-i] == side)
    return max(resultSheet)
             
def backtracking(board, dictionary, isFirst = False):
    if(len(dictionary["O"]) == 0 and len(dictionary["X"]) == 0):
        return True
       
    if(isFirst == False):
        if(isEnd("O", board) == 1 or isEnd("X", board) == 1):
            return False
        
    # print(board, isFirst, isEnd("O", board), isEnd("X", board) == 1)
    
    diff = len(dictionary["O"]) - len(dictionary["X"])
    
    if(diff == 0):
        currentSide = "X"
    elif(diff == 1):
        currentSide = "O"
    else:
        return False
        
    result = []
    for i in range(len(dictionary[currentSide])):
        a, b = dictionary[currentSide][i]
        newBoard = [i[:] for i in board]

        newBoard[a][b] = "."
        newdict = copy.deepcopy(dictionary)
        newdict[currentSide] = dictionary[currentSide][: i] + dictionary[currentSide][i+1 :]
        result.append(backtracking(newBoard, newdict))
    return max(result)
        
            
    
        
def solution(board):
    dictionary = {"O" : [], "X" : []}
    for i in range(3):
        board[i] = list(board[i])
        for j in range(3):
            if(board[i][j] != "."):
                dictionary[board[i][j]].append([i, j])
            
    return int(backtracking(board, dictionary, True))
    
                
            
        
            