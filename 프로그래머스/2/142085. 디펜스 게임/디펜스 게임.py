import heapq

def solution(n, k, enemy):
    enemy_sum = 0
    i = 0
    heap = []
    # heap에 enemy 추가
    # n 보다 총합이 커지면, k를 써서 heap에서 꺼냄
    # k가 0보다 작으면 그대로 둠
    while(i < len(enemy) and enemy_sum <= n):
        heapq.heappush(heap, -enemy[i])
        enemy_sum += enemy[i]
        while(k > 0 and enemy_sum > n and heap):
            k -= 1
            enemy_sum += heapq.heappop(heap)
        # print(heap)
        if(enemy_sum > n):
            break
        i += 1
        
    answer = i
    return answer