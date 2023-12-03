# 지금 후자가 더 크다 => 후자에서 하나 빼기
# 지금 전자가 더 크다 => 전자에서 하나 빼기

# 그렇다면 원소의 합을 같게 만들 수 없는 경우는? 
#ex) [1, 1, 1, 1, 1], [1, 1, 1, 9, 1] => 3n까지 확인

from collections import deque

def solution(queue1, queue2):
    answer = 0
    number = 3*len(queue1)
    q1_sum = sum(queue1)
    q2_sum = sum(queue2)
    q1 = deque(queue1)
    q2 = deque(queue2)
    while(answer < number):
        if(q1_sum < q2_sum): #q2꺼 빼서 p1에 넣기
            q1_sum += q2[0]
            q2_sum -= q2[0]
            q1.append(q2.popleft())
        elif(q1_sum > q2_sum): #q1꺼 빼서 p2에 넣기
            q2_sum += q1[0]
            q1_sum -= q1[0]
            q2.append(q1.popleft())
        else:
            return answer
        answer += 1
    return -1

