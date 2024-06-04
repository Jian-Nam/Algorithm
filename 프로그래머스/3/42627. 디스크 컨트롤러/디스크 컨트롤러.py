import heapq
def solution(jobs):
    heap = list()
    
    timesum = 0
    endingtime = 0
    requestindex = 0
    popcount = 0
    jobs.sort(key = lambda x : (x[0], x[1]))

    while (popcount < len(jobs)):
        while((requestindex< len(jobs)) and (jobs[requestindex][0]<=endingtime or len(heap) == 0)):
            heapq.heappush(heap, (jobs[requestindex][1], jobs[requestindex][0]))
            requestindex +=1
            # print(f"{endingtime}, {heap}")

        duration, request = heapq.heappop(heap)
        popcount +=1
        if(endingtime>request):
            timesum += endingtime - request
            endingtime += duration
        else:
            endingtime = request + duration
        timesum += duration


    return timesum//len(jobs)