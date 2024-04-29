from collections import defaultdict

def check(a, b):
    if(d[(a, b)] != -1):
        return d[(a, b)]
    for k in range(2, 5):
        for l in range(2, 5):
            if(a * k == b * l):
                d[(a, b)] = 1
                d[(b, a)] = 1
                return d[(a, b)]
    d[(a, b)] = 0
    d[(b, a)] = 0
    return d[(a, b)]
    
def solution(weights):
    global d
    d = defaultdict(lambda: -1)
    
    weightdict = {}
    
    for w in weights:
        weightdict[w] = weightdict.setdefault(w, 0) + 1
    key = list(weightdict.keys())

    answer = 0

    for i in range(len(key)):
        for j in range(i, len(key)):
            if(i == j):
                answer += (weightdict[key[i]]  * (weightdict[key[i]]-1))/2
                continue
            if(check(key[i], key[j])):
                print(key[i], key[j], weightdict[key[i]] * weightdict[key[j]])
                answer += weightdict[key[i]] * weightdict[key[j]]


    return answer