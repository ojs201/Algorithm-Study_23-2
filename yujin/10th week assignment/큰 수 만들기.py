# 시간 초과, combination의 시간 복잡도 : O(2^n)
from itertools import combinations

def solution(number, k):
    answer = list(combinations(number ,len(number)-k))
    new = ["".join(a) for a in answer]
    return max(new)

# ======================================================================================
def solution(number, k):
    stack = []
    for num in number:
        while k > 0 and stack and stack[-1] < num:
            stack.pop()
            k -= 1
        stack.append(num)
    return "".join(stack[:len(number) - k])