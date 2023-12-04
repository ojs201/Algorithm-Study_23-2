"""
LV2. 연속된 부분 수열의 합
[https://school.programmers.co.kr/learn/courses/30/lessons/178870]

유형:
완전 탐색/투 포인터

풀이:
1. sequence[s] + sequence[e] == k에 만족할 때까지 투 포인터 탐색을 진행한다.
2. <1>번 조건에 만족하는 경우 그에 해당하는 (s, e)를 저장한다.
3. 투 포인터 탐색이 끝난 후 아래를 기준으로 정렬한 뒤 첫 번째 원소의 (s, e)를 반환한다.
    1. 길이가 제일 짧으며
    2. 제일 먼저 나온 순
"""


def solution(sequence, k):
    answer = []

    n = len(sequence)
    s, e = 0, 0
    total = 0

    while s < n:
        if total >= k:
            total -= sequence[s]
            s += 1
        else:
            if e >= n:
                break

            total += sequence[e]
            e += 1

        if total == k:
            answer.append((s, e - 1))

    answer.sort(key=lambda x: (x[1] - x[0], x[0]))
    return [answer[0][0], answer[0][1]]
