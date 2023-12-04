"""
LV2. 메뉴 리뉴얼
[https://school.programmers.co.kr/learn/courses/30/lessons/72411]

풀이:
1. 하나의 코스요리 course[i]에 대해 다음을 적용한다.

    1.1. orders의 각 요소에서 course[i]에 해당하는 모든 조합의 수를 구한다.
        - 이때 각 조합의 동등 여부를 판별하기 위해 미리 오름차 순 정렬시킨다.
    1.2. 모든 조합의 수에서 가장 많이 나온 조합의 수를 구한다.
    1.3. 모든 조합의 수에서 아래 조건에 만족하는 모든 조합을 구한다.
        1.3.1 현재 조합의 개수 > 1
        1.3.2 현재 조합의 개수 == 가장 많이 나온 조합의 수

2. 위 <1> 번 과정을 모든 course에 대해 반복한다.
3. 위 <1> ~ <2> 번 과정을 반복하여 도출된 모든 조합의 수를 반환한다.
"""
from collections import Counter
from itertools import combinations


def solution(orders, course):
    answer = []

    for course_size in course:
        order_combs = []

        for order in orders:
            order_combs += combinations(sorted(order), course_size)

        most_ordered = Counter(order_combs).most_common()
        answer += [menu for menu, count in most_ordered if count > 1 and count == most_ordered[0][1]]

    return [''.join(menu) for menu in sorted(answer)]
