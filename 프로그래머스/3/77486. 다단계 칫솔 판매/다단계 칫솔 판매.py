from collections import defaultdict
def solution(enroll, referral, seller, amount):
    enroll_dict = {}
    sell_dict = {}
    profit_dict = defaultdict(int)
    
    for i, v in enumerate(enroll):
        enroll_dict[v] = referral[i]
    
    for i, v in enumerate(seller):
        profit = amount[i] * 100
        profit_dict[v] += profit
        
        current = v
        while(current != "-" and profit // 10 >= 1):
            parent = enroll_dict[current]
            profit //= 10
            profit_dict[current] -= profit
            profit_dict[parent] += profit
            current = parent
            
        

    answer = []
    for i in enroll:
        answer.append(profit_dict[i])
    return answer