"""
LV2. 연속 부분 수열 합의 개수
[https://school.programmers.co.kr/learn/courses/30/lessons/131701]

문제 분석:
- 어떠한 경우든 연속 부분의 수열의 합의 개수는 N개 이하이다.
- 부분 수열의 시작과 끝은 수열의 시작과 끝에 영향을 받지 않는다.
- 각 수열의 합에서 중복된 부분은 제외한다.
- 각 수열의 합의 개수를 셀 때 중복된 부분은 제외한다.

풀이:
- 부분 수열의 시작과 끝에 영향을 받지 않기 때문에 list slicing을 쓰기 어려움
- 이때 단순히 수열의 크기를 2배로 하면 리스트 slice 수행 시 문제에 영향을 받지 않음
- 따라서 수열의 크기를 배로 한 뒤 수열의 크기가 1 ~ N일 경우의 모든 연속 부분 수열의 합을 구한 뒤 개수를 반환
"""


def solution(elements):
    answer = set()
    n = len(elements)
    elements *= 2

    for i in range(n):
        for j in range(i + 1, i + n):
            answer.add(sum(elements[j:j + i]))
    return len(answer)
