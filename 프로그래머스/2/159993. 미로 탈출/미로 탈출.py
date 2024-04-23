from collections import deque, defaultdict

def findInMaps(maps, target):
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if(maps[i][j] == target):
                return [i, j]
    return [-1, -1]
                
def go(i, j, di, dj, mi, mj):
    ri = i + di
    rj = j + dj
    if(ri >= 0 and ri < mi and rj >= 0 and rj < mj):
        return [ri, rj]
    else:
        return [-1, -1]

def solution(maps):
    dxdy = [[1, 0],[0, 1],[-1, 0],[0, -1]]
    mi = len(maps)
    mj = len(maps[0])
    starti, startj = findInMaps(maps, "S")
    
    def bfs(starti, startj, target):
        visited = [[-1] * mj for _ in range(mi)]
        que = deque()
        que.append([starti, startj])
        visited[starti][startj] = 0

        while(que):
            # print(que)
            i, j = que.popleft()
            if(maps[i][j] == target):
                return [i, j, visited[i][j]]
            
            for l in range(4):
                di, dj = dxdy[l]
                nexti, nextj = go(i, j, di, dj, mi, mj)
                # print(i, j, di, dj, nexti, nextj)
                if(nexti != -1 and nextj != -1 and visited[nexti][nextj] == -1 and maps[nexti][nextj] != "X"):
                    que.append([nexti, nextj])
                    visited[nexti][nextj] = visited[i][j] + 1
        return [-1, -1, -1]
                
    li, lj, distance1 = bfs(starti, startj, "L")
    if(distance1 != -1):
        _, _, distance2 = bfs(li, lj, "E")
        if(distance2 != -1):
            return distance1 + distance2
    return -1