def recursion(words, times):
    count = 0
    global aldict
    recursion_list = [[] for i in range(26)]
    for w in words:
        if(len(w) < times + 1):
            count += times
            continue
        recursion_list[aldict[w[times]]].append(w)
    
    for l in recursion_list:
        if len(l) == 0:
            continue
        if len(l) == 1:
            count += times + 1
        else:
            count += recursion(l, times + 1)
            
    return count
            

def solution(words):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    global aldict
    aldict = {}
    for i, v in enumerate(alphabet):
        aldict[v] = i

    return recursion(words, 0)