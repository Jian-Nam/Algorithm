def solution(A, B):
    # A, B 정렬
    A.sort()
    B.sort()
    
    # 투포인터
    a = 0
    b = 0
    
    count = 0
    while(a < len(A) and b < len(B)):
        if(A[a] < B[b]):
            count += 1
            a += 1
            b += 1
        else:
            b += 1
    
    return count