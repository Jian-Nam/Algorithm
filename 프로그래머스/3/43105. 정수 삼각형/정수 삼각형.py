def maxValue(i, j, triangle):
    if(j-1<0):
        return(triangle[i-1][j])
    if(j>(i-1)):
        return(triangle[i-1][j-1])
    return max(triangle[i-1][j-1], triangle[i-1][j])
    
def solution(triangle):
    height = len(triangle)
        
    for i in range(1, height):
        layer = triangle[i]
        for j in range(len(layer)):
            triangle[i][j] += maxValue(i, j, triangle)

    return max(triangle[-1])