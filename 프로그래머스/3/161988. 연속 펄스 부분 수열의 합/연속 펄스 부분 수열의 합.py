def solution(sequence):
    cum_seq1 = [sequence[0]]
    cum_seq2 = [- sequence[0]]
    for i, s in enumerate(sequence):
        if(i == 0): continue
        if(i%2 == 0):
            cum_seq1.append(cum_seq1[i-1]+ s)
            cum_seq2.append(cum_seq2[i-1] -s)
        else:
            cum_seq1.append(cum_seq1[i-1] - s)
            cum_seq2.append(cum_seq2[i-1] + s)
    
    def get_max_sum(cum_seq):
        min_sum = 0
        max_sum = 0
        for i, s in enumerate(cum_seq):
            result = s - min_sum
            if(max_sum < result):
                max_sum = result
            if(s < min_sum):
                min_sum = s
                
        return max_sum
            
    # print(cum_seq1)
    # print(cum_seq2)
    # print(get_max_sum(cum_seq1))
    # print(get_max_sum(cum_seq2))
    return max(get_max_sum(cum_seq1), get_max_sum(cum_seq2))