def solution(numbers):
    answer = [-1] * len(numbers)
    
    stack = []
    stack.append([0, numbers[0]])
    for i in range(1, len(numbers)):
        while(stack and numbers[i] > stack[-1][1]):
            index, n = stack.pop()
            answer[index] = numbers[i]
        stack.append([i, numbers[i]])
        
    return answer