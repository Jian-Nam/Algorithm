from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    matrix = [[1] * 101 for i in range(101)]

    
    # 내부 = 0 선 = 2 외부 = 1
    for lbx, lby, rtx, rty in rectangle:
        lbx *= 2
        lby *= 2
        rtx *= 2
        rty *= 2
        for ix in range(lbx, rtx + 1):
            for iy in range(lby, rty + 1):
                if(ix in [lbx, rtx] or iy in [lby, rty]):
                    matrix[ix][iy] *= 2
                else:
                    matrix[ix][iy] *= 0
    
    visited = [[-1] * 51 for i in range(51)]
    
    que = deque()
    que.append([characterX, characterY])
    visited[characterX][characterY] = 0
    # print(matrix)
    
    directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    while(que):
        x, y = que.popleft()
        # print(x, y, visited[x][y])
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            # 윤곽선 확인 표를 2배로 만들어 좌표 사이가 비었는지 확인, 1단위로 하면 건너뛸 수 있음
            if(nx >= 0 and nx <= 50 and ny >= 0 and ny <=50 and visited[nx][ny] == -1 and matrix[nx * 2 - dx][ny * 2 - dy] > 1):
                visited[nx][ny] = visited[x][y] + 1
                que.append([nx, ny])
                if(nx == itemX and ny == itemY):
                    return visited[nx][ny]

    answer = 0
    return answer