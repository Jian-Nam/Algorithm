def gcd(a, b):
    remain = None
    left = a if a > b else b
    right = b if a > b else a
    
    while(remain != 0):
        remain = left % right
        left = right
        right = remain
        
    return left

def possible(arrayA, arrayB):
    gcdA = arrayA[0]
    for i in range(1, len(arrayA)):
        gcdA = gcd(arrayA[i], gcdA)
        
    for b in arrayB:
        if b % gcdA == 0:
            return 0
    return gcdA
        
def solution(arrayA, arrayB):
        
    return max(possible(arrayA, arrayB), possible(arrayB, arrayA))