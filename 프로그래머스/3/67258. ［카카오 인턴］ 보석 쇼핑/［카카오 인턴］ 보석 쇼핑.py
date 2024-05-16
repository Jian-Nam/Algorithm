from collections import defaultdict
def solution(gems):
    start = 0
    end = 0
    answer = [0, len(gems) - 1]
    
    max_type = len(set(gems))
    type_count = defaultdict(int)
    type_count[gems[0]] += 1
    
    types_now = 1
    
    while(start <= end and end < len(gems) and start < len(gems)):
        # print(start, end, types_now, max_type, type_count)
        if(types_now >= max_type):
            if(end - start < answer[1] - answer[0]):
                answer[0] = start
                answer[1] = end
            type_count[gems[start]] -= 1
            if(type_count[gems[start]]== 0):
                types_now -= 1
            start += 1
        else:
            end += 1
            if(end < len(gems)):
                if(type_count[gems[end]] == 0):
                    types_now += 1
                type_count[gems[end]] += 1


    answer[0] += 1
    answer[1] += 1
    return answer