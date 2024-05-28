def recursion(arr, rowStart, rowEnd, colStart, colEnd):
    answer = [0]*2
    length = rowEnd - rowStart
    if(length == 1):
        value = arr[rowStart][colStart]
        answer[value] = 1
        return answer
    
    nextLength = int(length/2)
    for i in range(2):
        for j in range(2):
            result = recursion(arr, 
                      rowStart + i * nextLength, 
                      rowStart + i * nextLength + nextLength,
                      colStart + j * nextLength,
                      colStart + j * nextLength + nextLength)
            answer[0] += result[0]
            answer[1] += result[1]
    
    if(answer[0] == 4 and answer[1] == 0):
        return [1, 0]
    if(answer[1] == 4 and answer[0] == 0):
        return [0, 1]
    return answer
    
            
    

def solution(arr):
    return recursion(arr, 0, len(arr), 0, len(arr))