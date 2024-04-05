import heapq

def solution(plans):
    heap = []
    for i in plans:
        time = i[1].split(":")
        subject = i[0]
        startTime = int(time[0]) * 60 + int(time[1])
        duration = int(i[2])
        heapq.heappush(heap, [startTime, duration, subject])
        
    print(heap)
    answer = []
    stack = []
    
    def doRemainjobs(remainTime):
        while(len(stack)>0):
            tempTask = stack.pop()
            remainTime -= tempTask[1]
            if(remainTime<0):
                tempTask[1] = -remainTime
                stack.append(tempTask)
                return
            answer.append(tempTask[2])
        
    
    task = heapq.heappop(heap)
    while(len(heap)>0):
        newTask = heapq.heappop(heap)
        distance = newTask[0] - task[0]
        task[1] -= distance
        if(task[1] > 0):
            stack.append(task)
        else:
            answer.append(task[2])
            remainTime = -task[1]
            doRemainjobs(remainTime)
        task = newTask
        
    answer.append(task[2])
    while(len(stack)>0):
        answer.append(stack.pop()[2])

    return answer