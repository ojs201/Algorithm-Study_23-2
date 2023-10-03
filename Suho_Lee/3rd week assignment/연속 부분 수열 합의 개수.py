# 나의 1차 풀이 -> 완전탐색(brute force)
# 시간초과 발생

def solution(elements):
    
    sum_li = [] # 연속 부분 수열 합을 넣을 리스트
    
    db_elements = elements * 2 #현재 리스트를 하나 더 이어붙임.
    
    # 완전 탐색으로 모든 경우의 수를 다 고려하고, 중복되지 않으면 sum_li에 추가
    for i in range(0, len(elements)): 
        for j in range(1, len(elements)+1):
            tmp = sum(db_elements[i:i+j])

            # <이 부분이 시간초과의 원인>
            if tmp not in sum_li:
                sum_li.append(tmp)
    
    return len(sum_li)





        
# 나의 두번째 풀이
# : 리스트 길이를 늘린 동일 방법이지만, 이중 포문 안에 한번 더 sum_li를 순회하는 코드 제거함.
# : 시간 초과 해결
def solution(elements):
    sum_li = set()

    db_elements = elements * 2
    
    for i in range(0, len(elements)):
        for j in range(0, len(elements)):
            sum_li.add(sum(db_elements[j:j+i+1]))
    return len(sum_li)








# 다른 사람 풀이
# 회전 큐(circular Queue)를 사용한 풀이
# 매 회전 마다 부분 합을 따로 구하게 되면, 결국 전체 부분합 경우를 모두 고려할 수 있다.
# deque.rotate(1) == list[i:] + list[:i]

from collections import deque
 
def solution(elements):
    answer = set()
    elements = deque(elements)
    for j in range(len(elements)):
        elements.rotate(1)
        for i in range(1,len(elements)):
            answer.add(sum(list(elements)[:i]))
    answer.add(sum(elements))
    return len(answer)