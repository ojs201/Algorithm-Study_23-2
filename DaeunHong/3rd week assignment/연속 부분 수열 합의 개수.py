# 연속 부분 수열 합의 개수
# https://school.programmers.co.kr/learn/challenges?order=acceptance_desc&levels=2&languages=python3

def solution(elements):
    answer = set()
    N = len(elements)
    elements = 2 * elements
    for limit in range(1, N+1):
        for i in range(N):
            answer.add(sum(elements[i:i+limit]))
    return len(answer)

# 위 풀이 코드 줄이기
def solution(elements):
    N = len(elements)
    elements = 2 * elements
    answer = [sum(elements[i:i + limit]) for limit in range(1, N + 1) for i in range(N)]
    return len(set(answer))

# dp 이용한 풀이 위 두가지 풀이보단 이 풀이가 가장 나아보임.
def solution(elements):
    N = len(elements)
    dp = elements[:]
    elements = 2 * elements
    answer = set(dp)
    for i in range(2, N):
        for j in range(N):
            dp[j] = dp[j] + elements[j+i-1]
            answer.add(dp[j])
    return len(answer) + 1