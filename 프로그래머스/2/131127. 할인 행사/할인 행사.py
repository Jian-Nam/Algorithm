def check(want, number, window):
    for i, w in enumerate(want):
        if(window.get(w, 0) < number[i]):
            return False
    return True

def solution(want, number, discount):
    total_num = sum(number)
    
    window = {}
    for i in range(total_num):
        product = discount[i]
        window[product] = window.get(product, 0) + 1
    
    count = 0
    if(check(want, number, window)):
        count += 1
    for i in range(len(discount) - total_num):
        old = discount[i]
        new = discount[total_num + i]
        window[old] = window.get(old, 0) - 1
        window[new] = window.get(new, 0) + 1
        if(check(want, number, window)):
            count += 1
            
    return count