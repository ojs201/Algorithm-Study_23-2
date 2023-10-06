"""
LV2. 할인 행사
[https://school.programmers.co.kr/learn/courses/30/lessons/131127]

풀이:
1. 1번째 날부터 n번째 날까지 다음을 수행하며 할인 받을 수 있는 날짜의 총 일수를 센다.
	1.1 i번째 날에 대해 want에 대해 아래의 조건에 만족하면 원하는 제품을 모두 할인받을 수 있다.
		1.1.1 i부터 (i+10) 날까지 discount에서 want[j]인 경우를 센다.
	    1.1.2 이때 센 개수가 number보다 크거나 같다면 조건에 만족하면 True 아니면 False를 반환한다.
    1.2 만약 모든 want에 대해 True인 경우 할인 받을 수 있는 날짜 일수에 +1을 한다.
2. 모두 할인 받을 수 있는 날짜의 총 일수를 반환한다.
"""


def solution(want, number, discount) -> bool:
    return sum(is_all_discounted(want, number, discount[day:day + 10]) for day in range(len(discount)))


def is_all_discounted(want, number, discount) -> bool:
    return all(discount.count(product) >= quantity for product, quantity in zip(want, number))
