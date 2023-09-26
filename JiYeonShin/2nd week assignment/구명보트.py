from collections import deque

def solution(people, limit):
    answer = 0
    people.sort()
    dq = deque(people)
    while(dq):
        l = dq.popleft()
        answer += 1
        while(dq):
            w = dq.pop()
            if(l + w <= limit):
                break
            else:
                answer += 1
    return answer

#무게 제한이 100일 때, 최대한 100KG을 꽉꽉 채워서 내보내야 한다.
#오름차순 정렬 후, 제일 가벼운 사람 + 가장 무거운 사람 중 100KG 안 넘으면 OK
#가장 가벼운 사람이랑 더했는데도 100초과? 걍 혼자 타야하는 사람임