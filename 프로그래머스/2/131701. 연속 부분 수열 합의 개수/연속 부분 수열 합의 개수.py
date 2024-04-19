

def solution(elements):
    result = set()
    cum_sum = []
    cum_sum.append(0)
    for i,e in enumerate(elements):
        cum_sum.append(cum_sum[-1] + e)
    
    def get_sum(start_index, length):
        left_start = start_index
        left_end = min(start_index + length , len(elements))
        right_start = 0
        right_end = max(start_index + length - len(elements), 0)
        # print(left_start, left_end, right_start, right_end)
        return cum_sum[left_end] - cum_sum[left_start] + cum_sum[right_end] - cum_sum[right_start]
        
    
    for i in range(len(elements)):
        for l in range(len(elements)):
            result.add(get_sum(i,l))
    return len(result)