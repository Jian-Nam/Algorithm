import sys
sys.setrecursionlimit(10**9)

def traverse(oil_id, i, j):
    global id_map
    global my_land
    global range_map
    

    stack = []
    stack.append([i, j])
    
    oil_amount = 1
    id_map[i][j] = oil_id
    range_map[j].add(oil_id)
    direction = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    
    while(stack):
        ci, cj = stack.pop()
        for di, dj in direction:
            ni = ci + di
            nj  = cj + dj
            if(ni < len(my_land) and ni >= 0 and nj < len(my_land[0]) and nj >= 0):
                if(my_land[ni][nj] == 1 and id_map[ni][nj] == None):
                    id_map[ni][nj] = oil_id
                    range_map[nj].add(oil_id)
                    oil_amount += 1
                    stack.append([ni, nj])
                
    return oil_amount

def solution(land):
    global id_map
    global my_land
    global range_map
    oil_amount = {}
    id_map = [[None for j in range(len(land[0]))] for i in range(len(land))]
    my_land = land
    range_map = [set() for j in range(len(my_land[0]))]

    
    oil_id = 1
    for i, row in enumerate(land):
        for j, v in enumerate(row):
            if(v == 1 and id_map[i][j] == None):
                oil_amount[oil_id] = traverse(oil_id, i, j)
                oil_id += 1
    # print(id_map)
    # print(oil_amount)
    # print(range_map)
    
    max_oil = 0
    for ois in range_map:
        total_oil = 0
        for oi in ois:
            total_oil += oil_amount[oi]
        max_oil = total_oil if total_oil > max_oil else max_oil
            
    return max_oil