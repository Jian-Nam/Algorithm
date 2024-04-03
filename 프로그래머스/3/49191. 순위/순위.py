def traverse(w_or_l, me, result_dict):
    visited = [0 for i in range(len(result_dict))]
    stack = []
    answer = []
    stack.append(me)
    
    while(stack):
        c = stack.pop()
        for n in result_dict[c][w_or_l]:
            if visited[n] == 0:
                visited[n] = 1
                stack.append(n)
                answer.append(n)
                
    return answer
    

def solution(n, results):
    # n개의 리스트 요소 딕셔너리{win: [], lose:[]}
    result_dict = [{"w": [], "l":[]} for i in range(n+1)]
    # print(result_dict)
    
    for win, lose in results:
        result_dict[win]["w"].append(lose)
        result_dict[lose]["l"].append(win)
    
    count = 0
    for i in range(1, n+1):
        win_list = traverse("w", i, result_dict)
        lose_list = traverse("l", i, result_dict)
        if(len(win_list) + len(lose_list) == n-1):
            count += 1
    
    return count