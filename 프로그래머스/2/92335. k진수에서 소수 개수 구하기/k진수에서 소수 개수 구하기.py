from collections import defaultdict

def is_sosu(n,memo):
    if(memo[n] != -1):
        return memo[n]
    
    if(n < 2):
        memo[n] = 0
        return memo[n]
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            memo[n] = 0
            return memo[n]
        
    memo[n] = 1
    return memo[n]
            
    
def to_k(number, k):
    result = []
    while(number > 0):
        result.append(number % k)
        number //= k
    return result
        
    
def solution(n, k):
    converted_number = to_k(n, k)
    numbers = []
    number = 0
    factor = 0
    
    for c in converted_number:
        if(c == 0 and number != 0):
            numbers.append(number)
            number = 0
            factor = 0
        elif(c != 0):
            number += c * (10**factor)
            factor += 1
    numbers.append(number)
    
    # print(converted_number)
    # print(numbers)
    memo = defaultdict(lambda:-1)
    count = 0
    for n in numbers:
        if(is_sosu(n, memo)):
            count += 1
    return count