def remove110(list_string):
    i = 0
    count110 = 0
    result = []
    
    stack = []
    for i in range(len(list_string)):
        if(list_string[i] == "0" and len(stack) >= 2 and stack[-2] == "1" and stack[-1] == "1"):
            for i in range(2): stack.pop()
            count110 +=1
            continue
        stack.append(list_string[i])
            
    return [count110, stack]
            

def solution(s):
    answer = []
    for v in s:
        count, not110 = remove110(list(v))
        stack = 0
        insert_point = 0
        while(insert_point < len(not110)):
            if(not110[insert_point] == "0"):
                insert_point += 1
            elif(insert_point + 1 < len(not110) and not110[insert_point + 1] == "0"):
                insert_point += 1
            else:
                break
        
        result = ""
        for i in range(insert_point):
            result += not110[i]
        result += "110" * count
        for i in range(insert_point, len(not110)):
            result += not110[i]
        answer.append(result)
    return answer