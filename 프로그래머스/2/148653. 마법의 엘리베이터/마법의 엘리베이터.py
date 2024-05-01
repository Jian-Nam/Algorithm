def solution(storey):
    stoneT = 0
    while(storey):
        print(storey)
        remain2 = (storey % 100) // 10
        remain = storey % 10
        
        stone = remain if remain < (10 - remain) else (10-remain)
        stoneT += stone
        if(stone != remain):
            storey += stone
        else:
            if(remain == 5 and remain2 >=5 ):
                storey += stone
            else:
                storey -= stone
        storey //= 10
    return stoneT