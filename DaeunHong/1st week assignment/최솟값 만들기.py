# 최솟값 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/12941

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)
answer = 0

for i in range(0, len(A)):
    answer += A[i] * B[i]

print(answer)

"""
# 한줄 풀이
def getMinSum(A, B):
    return sum([a * b for a, b in zip(sorted(A), sorted(B, reverse=True))])

print(getMinSum([1, 2], [3, 4]))


# 시간초과
from itertools import permutations

A = list(map(int, input().split()))
B = list(map(int, input().split()))

data= []

for perm in permutations(A):
    result = 0
    for i in range (0, len(A)):
        result += perm[i] * B[i]
    data.append(result)

print(min(data))
"""






