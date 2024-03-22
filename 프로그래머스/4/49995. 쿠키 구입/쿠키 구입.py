def solution(cookie):
    cum = [0]
    
    tmp = 0
    for c in cookie:
        tmp += c
        cum.append(tmp)
    
    posible_max = cum[-1] // 2
    
    maximum = 0
    
    # 해당 인덱스 이전까지의 합
    for mid, mid_cum in enumerate(cum):
        start, end = mid-1, mid+1 # left: mid-1, right: mid
        while(start >= 0 and end < len(cum)):
            left = cum[mid] - cum[start] # cookie start 이상 mid 미만
            right = cum[end] - cum[mid] # cookie mid 이상 end 미만
            if(left > posible_max or right > posible_max):
                break
            if(left == right):
                maximum = left if left > maximum else maximum
                start -= 1
            elif(left > right):
                end += 1
            else:
                start -= 1
    
    return maximum