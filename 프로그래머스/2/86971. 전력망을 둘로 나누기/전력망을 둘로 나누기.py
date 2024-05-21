from collections import defaultdict
import copy

def solution(n, wires):

    wireDict = defaultdict(list)

    # make dict
    for i in wires:
        wireDict[i[0]].append(i[1]) 
        wireDict[i[1]].append(i[0])
        
    # dfs
    visited = [0]*n
    def countElement(graph, element):
        visited[element-1] = 1
        
        count = 1
        for i in graph[element]:
            if(visited[i-1] == 0):  
                count += countElement(graph, i)

        return count
    
    # 구현
    minimum = n-2
    for i in wires:
        subWireDict = copy.deepcopy(wireDict)
        subWireDict[i[0]].remove(i[1])
        subWireDict[i[1]].remove(i[0])
        
        visited = [0]*n
        a = countElement(subWireDict, i[0])
        
        visited = [0]*n
        b = countElement(subWireDict, i[1])
        if (minimum > abs(a-b)):
            minimum = abs(a-b)
    answer = minimum
    return answer