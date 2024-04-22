import sys
sys.setrecursionlimit(10**9)
def dfs(i, j, total):
    global gmaps
    total += gmaps[i][j]
    gmaps[i][j] = 0
    
    didj = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    for di, dj in didj:
        ni = i + di
        nj = j + dj
        if(ni >= 0 and ni < len(gmaps) and nj >= 0 and nj < len(gmaps[0])):
            if(gmaps[ni][nj] > 0):
                total = dfs(ni, nj, total)
    
    return total
    

def solution(maps):
    global gmaps
    gmaps = maps
    
    for i in range(len(gmaps)):
        gmaps[i] = list(gmaps[i])
        for j in range(len(maps[0])):
            if(gmaps[i][j] == 'X'):
                gmaps[i][j] = 0
            else:
                gmaps[i][j] = int(gmaps[i][j])
    # print(maps)
                
    answer = []
    for i in range(len(gmaps)):
        for j in range(len(gmaps[0])):
            if(gmaps[i][j] > 0):
                answer.append(dfs(i, j, 0))
                
    if(len(answer) == 0):
        return [-1]
    answer.sort()
    return answer