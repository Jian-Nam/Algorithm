import math
def solution(r1, r2):
    # -r1 ~ r1
    spot_count = 0
    for i in range(-r2, r2+1):
        r2_range = math.floor((r2**2-i**2)**(0.5))
        spot_count += 2*r2_range+1

        if(i>=-r1 and i<=r1):
            raw_r1_range= (r1**2-i**2)**(0.5)
            r1_range = math.floor(raw_r1_range)
            spot_count -= 2*r1_range+1
            if(raw_r1_range == r1_range):
                if(raw_r1_range == 0):
                    spot_count+=1
                else:
                    spot_count+=2

        
                
    return spot_count