"""
LV2. 구명보트 (해결 X)
[https://school.programmers.co.kr/learn/courses/30/lessons/42885]

풀이:
1. 각 사람의 몸무게를 오름차 순으로 정렬한다.
2. 가장 무거운 사람을 보트에 태운다.
3. 가장 가벼운 사람을 보트에 태운다.
4. 무게의 합에 따라 다음을 진행한다:
    4-A. 무게 합 > 보트 무게 제한 => 가벼운 사람을 내리고, 보트를 출발시킨다.
    4-B. 무게 합 <= 보트 무게 제한 => 보트를 출발시키고, 카운트를 +1 증가시킨다.
5. (사람의 수 - 카운트)를 계산한 값을 반환한다.
"""


def solution(people, limit):
    people.sort()
    nums_people = len(people)
    nums_pair = 0

    start = 0
    end = nums_people - 1

    while start < end:
        if people[start] + people[end] <= limit:
            nums_pair += 1
            start += 1
        end -= 1

    return nums_people - nums_pair
