import heapq

def solution(cards):
    # 카드를 한번 뽑았으면 그 숫자는 다시 나올 수 없으므로
    # 결국 처음 카드로 돌아오게 된다.
    visited = [0 for _ in range(len(cards)+1)]
    
    heap = []
    for i, c in enumerate(cards):   
        if(visited[c] == 1):
            continue
            
        boxi = c
        count = 0
        while(visited[boxi] != 1):
            visited[boxi] = 1
            boxi = cards[boxi-1]
            count += 1
        heapq.heappush(heap, -count)
    

    if(len(heap) > 1):
        return heapq.heappop(heap) * heapq.heappop(heap)
    else:
        return 0