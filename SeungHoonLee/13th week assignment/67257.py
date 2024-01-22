"""
LV2. 수식 최대화
[https://school.programmers.co.kr/learn/courses/30/lessons/67257]

[풀이]
1. 모든 경우의 연산자 우선 순위 집합을 구한다.
2. 각 경우에 대해 infix 연산을 적용 한다.
    - 이때 연산자 간의 우선 순위 결정은 주어진 우선 순위 집합에 따른다.
"""
import re
from itertools import permutations
from operator import add, sub, mul


def solution(expression):
    op_ranks = []
    for comb in permutations(['+', '-', '*'], 3):
        op_ranks.append({op: idx for idx, op in enumerate(comb)})

    tokens = re.split(r'(\D)', expression)
    return max([calculate(tokens, rank) for rank in op_ranks])


def calculate(expr, op_rank):
    operators = []
    values = []

    for token in expr:
        if token.isdigit():
            values.append(int(token))
        else:
            while operators and op_rank[operators[-1]] >= op_rank[token]:
                apply_operator(operators, values)
            operators.append(token)

    while operators:
        apply_operator(operators, values)
    return abs(values.pop())


def apply_operator(operators, values):
    op = {'+': add, '-': sub, '*': mul}
    operator = operators.pop()
    n2 = values.pop()
    n1 = values.pop()
    values.append(op[operator](n1, n2))
