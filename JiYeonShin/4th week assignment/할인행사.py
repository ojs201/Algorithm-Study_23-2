from collections import defaultdict

def solution(want, number, discount):
    answer = 0
    discountdict = defaultdict(int)
    for item in discount[0:10]:
        discountdict[item] += 1
    for day in range(len(discount)-10+1):
        #i번째 날이면 discount[i-1]에 있는거 -1하고 discount[10-1+i]에 있는거 +1
        if(day != 0):
            discountdict[discount[day-1]] -= 1
            discountdict[discount[10-1+day]] += 1
        for i in range(len(want)):
            if(discountdict[want[i]] < number[i]):
                break
        else:
            answer += 1  
    return answer