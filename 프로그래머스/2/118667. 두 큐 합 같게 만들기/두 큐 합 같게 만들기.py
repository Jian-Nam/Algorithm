from collections import deque

def solution(queue1, queue2):
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    diff = sum1 - sum2
    
    queue = queue1 + queue2

    start1 = 0
    start2 = len(queue2)
    
    depth = 0
    while(depth < 2 * len(queue)):
        if(diff == 0):
            return depth
        elif(diff > 0):
            diff -= queue[start1] * 2
            start1 += 1
            if(start1 >= len(queue)):
                start1 -= len(queue)
        else:
            diff +=  queue[start2] * 2
            start2 += 1
            if(start2 >= len(queue)):
                start2 -= len(queue)
        depth += 1
            

        
    return -1