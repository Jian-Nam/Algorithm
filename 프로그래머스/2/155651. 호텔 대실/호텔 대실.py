import heapq
def solution(book_time):
    books = []
    for start, finish in book_time:
        s_hour, s_minute = start.split(":")
        f_hour, f_minute = finish.split(":")
        start = int(s_hour)* 60 + int(s_minute)
        finish = int(f_hour) * 60 + int(f_minute) + 10
        heapq.heappush(books, [start, finish])
        
    rooms = []
    rooms.append([0, 0])
    while(books):
        start, finish = heapq.heappop(books)
        is_enough = False
        for i in range(len(rooms)):
            checkin, checkout = rooms[i]
            if checkout <= start:
                rooms[i] = [start, finish]
                is_enough = True
                break
        if(is_enough == False):
            rooms.append([start, finish])
        
    return len(rooms)