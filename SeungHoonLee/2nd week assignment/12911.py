"""
LV2. 다음 큰 숫자
[https://school.programmers.co.kr/learn/courses/30/lessons/12911]

풀이:
- '다음 큰 숫자'의 조건은 결국 이진수 변환 시 1의 개수가 서로 같은 수 중
  큰 수를 찾는 문제
- 이때 문제에서 주어진 최대 n의 값은 1,000,000이다.
- 이때 이진수의 특성상 특정한 숫자 n이 주어졌을 때 위 '다음 큰 숫자'를 만족하는 최대값은
  2*n이 된다.
- 따라서 (n+1) 부터 (2*n)까지 반복하며 '다음 큰 숫자'를 찾는다.

e.g.
2 ~ 4
(0010 ~ 0010)

4 ~ 8
(0100 ~ 1000)

12 ~ 24
(1100 ~ 1 0100)

83 ~ 166
(101 0011 ~ 1010 0110)
"""


def solution(n):
    n_ones = nums_one(n)
    return next(i for i in range(n + 1, 2 * n + 1) if n_ones == nums_one(i))


def nums_one(num):
    return dec_to_bin(num).count('1')


def dec_to_bin(num):
    return bin(num).replace('0b', '')
