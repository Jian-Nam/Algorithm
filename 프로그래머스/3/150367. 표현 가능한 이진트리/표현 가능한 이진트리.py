def solution(numbers):
    dp = {}
    dp[1] = 1
    dp[0] = 1
    def get_binary(num):
        binary = []

        while(num > 0):
            binary.append(num % 2)
            num //= 2
        
        full_len = 1
        while(len(binary) > full_len - 1):
            full_len *= 2
        
        while(len(binary) < full_len - 1):
            binary.append(0)
            
        return binary
    
    def split_binary(binary):

        stack = []
        stack.append(binary)
        while(stack):
            b = stack.pop()
            # print(binary, b)
            if(sum(b) == 0):
                continue
            mid = len(b) // 2
            if(b[mid] == 1):
                stack.append(b[:mid])
                stack.append(b[mid+1:])
            else:
                return 0
        return 1
        
    answer = []
    for n in numbers:
        binary = get_binary(n)
        answer.append(split_binary(binary))
    
    return answer