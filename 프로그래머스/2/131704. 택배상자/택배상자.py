def solution(order):
    stack = []
    belt = [i for i in range(len(order), 0, -1)]

    count = 0
    order.reverse()
        
    while(order):
        # print("o", order)
        # print("b", belt)
        # print("s", stack)
        if(belt and order[-1] == belt[-1]):
            belt.pop()
            order.pop()
            count +=1
            continue
        if(stack and order[-1] == stack[-1]):
            stack.pop()
            order.pop()
            count +=1
            continue
        if(belt):
            stack.append(belt.pop())
            continue
        break
            
        
    return count