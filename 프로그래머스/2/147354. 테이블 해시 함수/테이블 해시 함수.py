def solution(data, col, row_begin, row_end):
    def xor(a, b):
        result = 0
        count = 0
        while(a > 0 or b > 0):
            if(a % 2 != b % 2):
                result += 2 ** count
            a //= 2
            b //= 2
            count += 1
        return result
    data.sort(key = lambda x : (x[col-1], -x[0]))
    answer = 0
    for i in range(row_begin, row_end + 1):
        remains = 0
        for d in data[i-1]:
            remains += d % i
        answer = xor(answer, remains)
            
    return answer