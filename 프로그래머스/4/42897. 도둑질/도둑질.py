def solution(money):
    first_houseO = []
    first_houseX = []
    first_houseO.append(money[0])
    first_houseO.append(max(money[0], money[1]))
    first_houseX.append(0)
    first_houseX.append(money[1])
    
    for i, m in enumerate(money):
        if(i == 0 or i == 1): continue
        if(i == len(money) - 1):
            first_houseO.append(first_houseO[i-1])
            first_houseX.append(max(first_houseX[i-2] + m, first_houseX[i-1]))
            continue
        first_houseO.append(max(first_houseO[i-2] + m, first_houseO[i-1]))
        first_houseX.append(max(first_houseX[i-2] + m, first_houseX[i-1]))
    return max(first_houseO[-1], first_houseX[-1])