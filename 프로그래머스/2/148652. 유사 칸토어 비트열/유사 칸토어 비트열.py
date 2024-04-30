import sys

def solution(n, l, r):
    count = 0
    for i in range(l-1, r):
        tmp = i
        while(tmp > 0):
            if tmp % 5 == 2:
                count += 1
                break
            tmp //= 5
            
    return r-l+1-count