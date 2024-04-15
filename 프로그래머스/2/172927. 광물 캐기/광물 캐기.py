import heapq
class node:
    def __init__(self, diamond, iron, stone):
        self.diamond = diamond
        self.iron = iron
        self.stone = stone
        self.matrix = [[1, 1, 1],[5, 1, 1],[25, 5, 1]]
    
    def __lt__(self, other):
        if(self.diamond > other.diamond):
            return True
        elif(self.diamond == other.diamond):
            if(self.iron > other.iron):
                return True
            elif(self.iron == other.iron):
                return self.stone > other.stone
        else:
            return False
        
    def __str__(self):
        return f'{self.diamond}, {self.iron}, {self.stone}'
    
    def getTired(self, toolIndex):
            return self.matrix[toolIndex][0] * self.diamond + self.matrix[toolIndex][1] *self.iron + self.matrix[toolIndex][2] * self.stone


def solution(picks, minerals):
    picksCount = 0;
    for pick in picks:
        picksCount += pick
    # print(picksCount)
    
    heap = []
    for i in range(picksCount):
        area = minerals[i*5 : min((i+1)*5, len(minerals))]
        diamond , iron, stone = [0, 0, 0]
        for m in area:
            if(m == "diamond"): diamond +=1
            elif (m == "iron"): iron += 1
            else: stone += 1
        heapq.heappush(heap, node(diamond, iron, stone))
        
    tired = 0
    while(heap):
        nowArea = heapq.heappop(heap)
        tool = 5
        for i in range(3):
            if (picks[i] > 0):
                tool = i
                picks[i] -= 1
                break
        tired += nowArea.getTired(tool)
        

    answer = tired
    return answer