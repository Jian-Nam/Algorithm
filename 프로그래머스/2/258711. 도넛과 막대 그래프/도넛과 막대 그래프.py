from collections import defaultdict

def solution(edges):
    pure_edges = defaultdict(list)
    reverse_edges = defaultdict(list)
    root = None
    
    for start, end in edges:
        pure_edges[start].append(end)
        reverse_edges[end].append(start)
    
    for node in pure_edges.keys():
        if(len(pure_edges[node]) >= 2 and len(reverse_edges[node]) == 0):
            root = node
            break
    
    
            
    def traverse(node):
        visited = defaultdict(int)
        stack = [node]
        while(stack):
            now = stack.pop()
            if(len(pure_edges[now]) == 0):
                return 2
            if(len(pure_edges[now]) == 2 and len(reverse_edges[now]) == 2):
                return 3

            for p in pure_edges[now]:
                if(visited[p] == 0):
                    visited[p] += 1
                    stack.append(p)
        return 1
              
    answer = [root, 0, 0, 0]      
    for node in pure_edges[root]:
        reverse_edges[node].remove(root)
        answer[traverse(node)] += 1
        
               
    

    return answer