"""
LV2. 괄호 변환
[https://school.programmers.co.kr/learn/courses/30/lessons/60058]
"""


def convert(w: str) -> str:
    """
    "올바른 괄호 문자열" 변환 알고리즘을 적용합니다.
    """
    if w == '' or is_balanced(w):
        return w

    u, v = split_uv(w)

    if is_balanced(u):
        return u + convert(v)

    return '(' \
        + convert(v) \
        + ')' \
        + reverse_brackets(u[1:-1])


def is_balanced(w: str) -> bool:
    """
    균형 잡힌 괄호 문자열인지 판별합니다.
    """
    cnt: int = 0
    return all(
        (cnt := cnt + 1 if ch == '(' else cnt - 1) >= 0
        for ch in w
    )


def split_uv(w: str) -> tuple:
    """
    "균형잡힌 괄호 문자열" u, v로 분리합니다.
    """
    cnt: int = 0

    for i, ch in enumerate(w):
        cnt += 1 if ch == '(' else -1

        if cnt == 0:
            return w[:i + 1], w[i + 1:]

    return '', ''


def reverse_brackets(w: str) -> str:
    """
    괄호 문자열의 괄호 방향을 반전시킨 결과를 반환합니다.
    """
    table = str.maketrans("()", ")(")
    return w.translate(table)


def solution(w):
    return convert(w)
