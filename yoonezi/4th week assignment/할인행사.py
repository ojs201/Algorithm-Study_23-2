from collections import Counter

def solution(want, number, discount):
    answer = 0
    wishList = {}
    
    for i in range(len(want)) :
        wishList[want[i]] = number[i]
    
    for i in range(len(discount)-9) :
        c = Counter(discount[i:i+10])
        
        if ( c == wishList) :
            answer += 1
            
    return answer