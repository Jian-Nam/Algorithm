def solution(friends, gifts):
    mtx = [[0] * len(friends) for i in range (len(friends))]
    gift_score = [0] * len(friends)
    for g in gifts:
        A, B = g.split(" ")
        Ai = None
        Bi = None
        for i in range(len(friends)):
            if(A == friends[i]):
                Ai = i
            if(B == friends[i]):
                Bi = i
        mtx[Ai][Bi] += 1
        gift_score[Ai] += 1
        gift_score[Bi] -= 1
        
        
    next_gifts = [0] * len(friends)
    
    for i in range(len(friends)):
        for j in range(i+1, len(friends)):
            if(mtx[i][j] > mtx[j][i]):
                next_gifts[i] += 1
            elif(mtx[i][j] < mtx[j][i]):
                next_gifts[j] += 1
            else:
                if(gift_score[i] > gift_score[j]):
                    next_gifts[i] += 1
                elif(gift_score[i] < gift_score[j]):
                    next_gifts[j] += 1
        
    return max(next_gifts)