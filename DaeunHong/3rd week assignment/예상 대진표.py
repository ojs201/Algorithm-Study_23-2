# 예상 대진표
# https://school.programmers.co.kr/learn/courses/30/lessons/12985

# 간결한 코드 2
n, a, b = map(int, input().split())
cnt = 0

while a != b:
    a, b, cnt = (a + 1) // 2, (b + 1) // 2, cnt + 1

print(cnt)

"""
# 첫 풀이
n, a, b = map(int, input().split())
cnt = 0

while a != b:
    if a % 2 == 0:
        a /= 2
    else:
        a = (a + 1) / 2

    if b % 2 == 0:
        b /= 2
    else:
        b = (b + 1) / 2

    cnt += 1


print(cnt)


# 간결한 코드 1
n, a, b = map(int, input().split())
cnt = 0

while a != b:
    a = (a + 1) // 2 if a % 2 else a // 2
    b = (b + 1) // 2 if b % 2 else b // 2
    cnt += 1

print(cnt)
"""






