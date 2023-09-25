# 1차 풀이 -> 37/100
# def solution(people, limit):
#     cnt = 0
    
#     sorted_ppl = sorted(people)
    
#     for i in range(len(sorted_ppl)-1):
#         if sorted_ppl[i] + sorted_ppl[i+1] <= limit:
#             cnt += 1
#             i += 2
    
#     cnt += (len(people) - cnt*2)
    
#     print(cnt)       
    
#     return cnt







# 2차풀이 37/100 
# 모든 경우를 다 나누었는데 실패...
# def solution(people, limit):
#     cnt = 0
#     sorted_ppl = sorted(people)
    
#     if (sorted_ppl[0] + sorted_ppl[1]) > limit:
#         cnt = len(people)
#     elif (sorted_ppl[0] + sorted_ppl[-1]) > limit:
#         for i in range(len(sorted_ppl)-1):
#             if sorted_ppl[i] + sorted_ppl[i+1] <= limit:
#                 cnt += 1
#         cnt += (len(people) - cnt*2)    
#     else:
#         for i in range(len(sorted_ppl)):
#             if (people[i] + people[-(i+1)]) <= limit:
#                 cnt += 1
#             else:
#                 break      
#         cnt += (len(people) - 2*cnt)
    
#     return cnt
    




# 3차 시도 : 덱으로 구현해야 한다는 힌트를 얻음.
from collections import deque

def solution(people, limit):
    dq = deque(sorted(people, reverse=True))
    cnt = 0 
    
    while len(dq)>1:
        if dq[0]+dq[-1]<=limit:
            cnt+=1
            dq.popleft()
            dq.pop()
        else:
            cnt+=1
            dq.popleft()
    
    if dq:
        cnt += 1
    
    return cnt