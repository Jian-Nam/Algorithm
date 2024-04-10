def solution(n, times):
    # 이상, 이하
    min_time = 1
    max_time = 1000000000000000000
    
    while(min_time < max_time):
        half = (max_time + min_time) // 2
        count = 0
        for t in times:
            count += half // t
        if(count >= n):
            max_time = half
        else:
            min_time = half+1

    return max_time