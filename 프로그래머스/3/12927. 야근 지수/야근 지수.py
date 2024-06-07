def solution(n, works):
    works.sort(reverse = True)
    
    index = 1
    while(n):
        while(index < len(works) and works[index-1] <= works[index]):
            index += 1
        for i in range(index):
            if(works[i] > 0): works[i] -= 1
            n -=1
            if(n <= 0):
                break
    
    print(works)
    sum = 0
    for i in works:
        sum += i**2
    
    return sum