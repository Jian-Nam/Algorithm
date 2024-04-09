from collections import defaultdict
import heapq

def solution(genres, plays):
    g_dict = defaultdict(list)
    cum_dict = defaultdict(int)
    
    for i, g in enumerate(genres):
        heapq.heappush(g_dict[g], [-plays[i], i])
        cum_dict[g] += plays[i]
    
    answer = []
    
    genre_order = []
    for k, v in cum_dict.items():
        heapq.heappush(genre_order, [-v, k])
    
    while(genre_order):
        _, key = heapq.heappop(genre_order)
        v = g_dict[key]
        for i in range(2):
            if(len(v) > 0):
                answer.append(heapq.heappop(v)[1])

    return answer