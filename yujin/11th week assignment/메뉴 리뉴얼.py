from itertools import combinations

def solution(orders, course):
    answer = []

    maxLen = len(max(orders, key=len))

    for c in course:
        if c > maxLen: continue
        checkTwoList = []
        checkTwoMax = 0
        for order in orders:
            if len(order) < c: continue
            splits = list(order)
            for comb in combinations(splits, c):
                checkTwo = 0

                for order in orders:
                    checkC = 0
                    for i in comb:
                        checkC += order.count(i)
                    if checkC >= c: checkTwo += 1
                if checkTwo >= 2:
                    if checkTwo > checkTwoMax: checkTwoMax = checkTwo
                    checkTwoList.append((checkTwo, ''.join(comb)))
        for i in checkTwoList:
            if i[0] == checkTwoMax:
                answer.append(i[1])
    for i in range(len(answer)):
        answer[i] = ''.join(sorted(answer[i]))
    answer = list(set(answer))    
    answer.sort()
    return answer