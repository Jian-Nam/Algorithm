import math
def solution(k, d):
    spot = 0
    for i in range(0, d + 1, k):
        remain = d**2 - i**2
        limit = int(math.sqrt(remain))
        
        #print(i, limit // k +1)
        spot += limit // k + 1

    return spot