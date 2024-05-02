def solution(cap, n, deliveries, pickups):
    
    total = 0
    
    while(deliveries and deliveries[-1] == 0):
        deliveries.pop()
        
    while(pickups and pickups[-1] == 0):
        pickups.pop()
    
    while(deliveries or pickups):
        distance = len(deliveries) if len(deliveries) > len(pickups) else len(pickups)
        total += distance * 2
        
        dremains = cap
        while(deliveries and deliveries[-1] <= dremains):
            dremains -= deliveries.pop()
        if(deliveries):
            deliveries[-1] -= dremains
        
        premains = cap
        while(pickups and pickups[-1] <= premains):
            premains -= pickups.pop()
        if(pickups):
            pickups[-1] -= premains
            
    
    answer = total
    return answer