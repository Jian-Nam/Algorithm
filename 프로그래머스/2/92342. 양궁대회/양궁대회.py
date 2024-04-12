def solution(n, info):
    info.reverse()
    dp = {}
    def back_tracking(remain, history):
        if(dp.get(tuple(history[:])) != None):
            return dp[tuple(history[:])]
        
        if(remain <= 0):
            score = 0
            for i in range(11):
                if(history[i] > info[i]):
                    score += i
                elif(info[i] > 0):
                    score -= i
            return [score, history]
        
        result = []
        for i in range(11):
            if(history[i] <= info[i]):
                nhistory = history[:] 
                nhistory[i] += 1
                result.append(back_tracking(remain-1, nhistory))
        if(result):
            dp[tuple(history[:])] = max(result)
            return dp[tuple(history[:])]
        else:
            dp[tuple(history[:])] = [-1, history]
            return dp[tuple(history[:])]
    
    answer = back_tracking(n, [0] * 11)
    if(answer[0] > 0):     
        answer[1].reverse()
        return answer[1]
    else:
        return [-1]