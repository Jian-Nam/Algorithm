def solution(targets):
    targets.sort(key = lambda x: (x[0], x[1]), reverse = True)
    
    misile = 0
    while(len(targets)>0):
        start, end = targets.pop()
        while(len(targets)>0 and targets[-1][0]< end):
            new_start, new_end = targets.pop()
            end = min(end, new_end)
        misile +=1
        
    return misile