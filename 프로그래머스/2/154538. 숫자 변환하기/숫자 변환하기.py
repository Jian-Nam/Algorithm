from collections import deque

def bfs(x, y, n):
    que = deque()
    que.append(x)
    
    visited = [-1] * (y+1)
    visited[x] = 0
    
    while(que):
        now = que.popleft()
        if(now == y):
            return visited[now]
        nextnums = [now * 2, now * 3, now + n]
        for num in nextnums:
            if(num <= y and visited[num] == -1):
                visited[num] = visited[now] + 1
                que.append(num)
                
    return -1
        
    

def solution(x, y, n):
    return bfs(x, y, n)