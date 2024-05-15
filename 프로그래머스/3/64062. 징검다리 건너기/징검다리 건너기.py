def is_possible(stones, num, k):
    count = 0
    for s in stones:
        if(s < num):
            count += 1
            if(count >= k): 
                return False
        else:
            count = 0
    return True

def solution(stones, k):
    end = max(stones)
    start = 0
    while(end != start):
        mid = (start + end) // 2 + 1
        if(is_possible(stones, mid, k)):
            start = mid
        else:
            end = mid - 1
            
    return start