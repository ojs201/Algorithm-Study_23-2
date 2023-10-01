# Counter() 사용하면 개수만큼 딕셔너리 형태로 제공
from collections import Counter

def solution(k, tangerine):
    answer = 0
    tangerine = Counter(tangerine) # 원소개수만큼 딕셔너리로 제공
        
    # items() , x[1] => 딕셔너리의 value 즉, 원소개수로 정렬.
    sorted_tangerine = sorted(tangerine.items(), key=lambda x:x[1], reverse=True)
    
    cnt = 0
    
    for i in sorted_tangerine:
        k-=i[1]
        answer += 1 #종류의 수가 늘어남.
        
        if k<=0:
            break
    
    return answer
    
    
        
    