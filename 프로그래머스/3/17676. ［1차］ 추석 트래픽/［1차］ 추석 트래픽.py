from collections import deque

def parse_time(log):
    _, time, duration = log.split()
    hour, minute, second = time.split(':')
    hour = int(hour)
    minute = int(minute)
    second = float(second)
    duration = float(duration[:-1])
    end = hour * 3600 + minute * 60 + second  
    start = end - duration + 0.001
    return(start, end)

def solution(lines):
    stack = []
    
    my_lines = []
    for log in lines:
        my_lines.append(parse_time(log))
    
    my_lines.sort()
    
    maximum = 0
    for log in my_lines:
        start, end = log
        while(stack and stack[-1][1] + 1 <= start):
            stack.pop()
        stack.append([start, end])
        stack.sort(key = lambda x: x[1], reverse = True)
        if(len(stack) > maximum):
            maximum = len(stack)
    
    return maximum