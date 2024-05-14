import heapq
import math

def hour2min(time):
    hour, minute = time.split(":")
    return int(hour) * 60 + int(minute)

def calculate(minute, fees):
    btime, bfee, utime, ufee = fees
    if(minute <= btime):
        return bfee
    else:
        return bfee + math.ceil((minute - btime)/utime) * ufee 
    

def solution(fees, records):
    table = {}
    for r in records:
        time, carnum, inout = r.split()
        time = hour2min(time)
        carnum = int(carnum)
        if(inout == "IN"):
            table[carnum] = table.get(carnum, [None, 0])
            table[carnum][0] = time
        else:
            table[carnum][1] += time - table[carnum][0]
            table[carnum][0] = None
    
    for carnum, value in table.items():
        if(value[0] != None):
            value[1] += hour2min("23:59") - value[0]
    
    nums = list(table.keys())
    nums.sort()

    
    answer = [calculate(table[n][1], fees) for n in nums]
    return answer