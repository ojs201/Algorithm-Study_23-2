from collections import Counter

def solution(k, tangerine):
    result = 0
    answer = 0
    
    tmp = Counter(tangerine)
    tmp = tmp.most_common()
    
    for i in tmp:
        result += i[1]
        answer += 1
        
        if(result >= k):
            return answer