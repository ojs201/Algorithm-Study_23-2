"""
LV2. 최솟값 만들기
[https://school.programmers.co.kr/learn/courses/30/lessons/12941]

풀이:
- 문제는 결국 두 리스트에서 i번째 요소들의 곱의 합을 구하는 문제
- 즉, 곱하기의 특성 상 문제의 최소의 합은
  하나를 오름차순, 다른 하나를 내림차순 으로 정렬하고 각 요소들을 곱한뒤 더한 값이다.
"""


def solution(A, B):
    # return min([reduce(lambda x, y: x + y[0] * y[1], zip(comb, B), 0) for comb in permutations(A, len(A))])
    return sum([a * b for a, b in zip(sorted(A), sorted(B, reverse=True))])
