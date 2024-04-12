def solution(k, ranges):
    cummulated_sum = []
    cummulated_sum.append(0)
    while(k != 1):
        nk = None
        if(k % 2 == 0):
            nk = k // 2
        else:
            nk = k * 3 + 1
        
        cummulated_sum.append(cummulated_sum[-1] + (nk + k) / 2)
        k = nk
    print(cummulated_sum)
    def get_result(s, e):
        if(len(cummulated_sum)-1 + e < s):
            return -1
        return cummulated_sum[len(cummulated_sum)-1 + e] - cummulated_sum[s]

    return [get_result(s, e) for s, e in ranges ]