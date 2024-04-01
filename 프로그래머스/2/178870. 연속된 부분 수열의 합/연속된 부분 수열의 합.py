def solution(sequence, k):
    start = len(sequence)
    end = len(sequence)-1
    sum = 0
    
    while(sum<k and start>=0):
        start -= 1
        sum += sequence[start]
        while(sum>k and end>=0):
            sum -= sequence[end]
            end -=1
    
    answer = [start, end]
    min_start = 0
    min_end = end-start
    sum2 = 0
    
    for i in range(min_end+1):
        sum2+=sequence[i]
        
    for i in range(len(sequence)-min_end-1):
        if sum2 == k:
            answer = [min_start, min_end]
            break
        sum2-= sequence[min_start]
        min_start +=1
        min_end +=1
        sum2 += sequence[min_end]
        
    return answer