from collections import defaultdict

def solution(topping):
    # 왼쪽은 set으로 충분 우측 개수 체크 필요
    left = set()
    t_dict = defaultdict(int)
    count = 0
    
    for t in topping:
        t_dict[t] += 1
    
    len_right = len(t_dict.keys())
    
    i = 0
    while(len(left) <= len_right):
        if(len(left) == len_right):
            count += 1
        t = topping[i]
        left.add(t)
        t_dict[t] -= 1
        if(t_dict[t] == 0):
            len_right -= 1
        i+=1
        
    
    return count