def solution(n, words):
    answer = [0, 0]


    for i in range(1, len(words)):
        if(words[i][0] != words[i-1][-1]):
            answer[0] = i%n+1
            answer[1] = i//n+1
            break
        elif(words[i] in words[:i-1]):
            answer[0] = i%n+1
            answer[1] = i//n+1
            break
        elif(len(words[i]) == 1):
            answer[0] = i%n+1
            answer[1] = i//n+1
            break

    return answer