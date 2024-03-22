def recursion(nums, operators):
    global dp
    # 메모이징
    if tuple(nums + operators) in dp.keys():
        return dp[tuple(nums + operators)]
    
    # 끝 도달
    if len(operators) == 0:
        dp[tuple(nums + operators)] = [nums[0], nums[0]]
        return dp[tuple(nums + operators)]
    
    minim = 1000000
    maxim = -1000000
    for i, o in enumerate(operators):
        left_min, left_max = recursion(nums[:i+1], operators[:i])
        right_min, right_max = recursion(nums[i+1:], operators[i+1:])
        new_minim = None
        new_maxim = None
        if o > 0:
            new_minim = left_min + right_min
            new_maxim = left_max + right_max
        elif o < 0:
            new_minim = left_min - right_max
            new_maxim = left_max - right_min
        minim = new_minim if new_minim < minim else minim
        maxim = new_maxim if new_maxim > maxim else maxim
        
    dp[tuple(nums + operators)] = [minim, maxim]
    return dp[tuple(nums + operators)]

def solution(arr):
    global dp
    dp = {}
    
    nums = []
    operators = []
    for i, v in enumerate(arr):
        if i % 2 == 0:
            nums.append(int(v))
        else:
            if(v == "+"):
                operators.append(1)
            else:
                operators.append(-1)
            
    return recursion(nums, operators)[1]