"""
LV2. 할인 행사
[https://school.programmers.co.kr/learn/courses/30/lessons/131127]

풀이:
1. 1번째 날부터 n번째 날까지 각 i번째 날에 대해 다음을 수행하여 할인 받을 수 있는 날짜의 총 일수를 센다.
  1.1. 아래의 조건에 만족하면 원하는 제품을 모두 할인 받을 수 있다.
    1.1.1. i부터 (i+10) 날까지 discount에서 원하는 품목(element of `want`)이 포함된 횟수를 센다.
	1.1.2. 위에서 구한 횟수가 number보다 크거나 같다면 True, 아니면 False를 반환한다.
  1.2. 만약 원하는 모든 품목(want)에 대해 위 조건이 True인 경우 할인 받을 수 있는 날짜 일수로 +1을 더한다.
2. 할인 받을 수 있는 날짜의 총 일수를 반환한다.
"""


def solution(want, number, discount) -> int:
    return sum(is_all_discounted(want, number, discount[day:day + 10]) for day in range(len(discount)))


def is_all_discounted(want, number, discount) -> bool:
    return all(discount.count(product) >= quantity for product, quantity in zip(want, number))
