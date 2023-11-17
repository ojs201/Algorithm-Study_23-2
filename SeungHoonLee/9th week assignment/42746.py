"""
LV2. 가장 큰 수
[https://school.programmers.co.kr/learn/courses/30/lessons/42746]

풀이:
1. numbers 내림차순 정렬을 수행한다.
    - 두 요소를 각각 문자열로 변환하여 비교한다.
    - 두 문자열의 길이가 다를 경우, 최대 비교 크기까지 자릿수를 맞춘다.
    - 문제에서 각 원소의 최대 길이는 4자리이므로, 두 문자열의 길이를 최소 4자리로 만든 뒤 정렬한다.

    - e.g. compare("3", "30") -> "3"이 더 높음
        - "3" -> "3333"
        - "30" -> "303030"

2. 정렬 시킨 문자열을 합친다.
3. 이때 numbers의 요소로 '0'이 올 수 있고, 입력이 ["0","0"]와 같은 경우 답은 "0"이므로 이를 처리한다.
"""


def solution(numbers):
    numbers.sort(key=lambda x: str(x) * 3, reverse=True)
    answer = ''.join(map(str, numbers))
    return '0' if answer[0] == '0' else answer
