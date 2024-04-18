from collections import defaultdict

def solution(k, tangerine):
    t_dic = defaultdict(int)
    for t in tangerine:
        t_dic[t] += 1
        
    t_items = list(t_dic.items())
    t_items.sort(key = lambda x : -x[1])
    
    count = 0
    i = 0
    while(i < len(t_items) and count < k):
        size, amount = t_items[i]
        count += amount
        i+= 1
        
    return i