def to_minute(time):
    hour, minute = time.split(":")
    return int(hour) * 60 + int(minute)

def add_0(number):
    if(number // 10 == 0):
        return "0" + str(number)
    else:
        return str(number)
    
def to_string(minute):
    return add_0(minute // 60) + ":" + add_0(minute % 60)
    
def solution(n, t, m, timetable):
    
    # 변환
    lines = []
    for time in timetable:
        lines.append(to_minute(time)) 
    lines.sort(reverse = True)
    
    bus = {}
    current = None
    for i in range(n):
        bus_time = 540 + i * t
        bus[bus_time] = []
        while(lines and lines[-1] <= bus_time and len(bus[bus_time]) < m):
            tmp = lines.pop()
            bus[bus_time].append(tmp)
            current =tmp
            
    bus_schedule = sorted(list(bus.keys()))
    
    if(len(bus[bus_schedule[-1]]) < m):
        return to_string(bus_schedule[-1])

    
    return to_string(current - 1)