# 이진 변환 반복하기
# https://school.programmers.co.kr/learn/courses/30/lessons/70129

import sys

data = str(sys.stdin.readline().rstrip())


def remove_zero(s):
    cnt = 0
    remove = [False] * len(s)
    for i in range(0, len(s)):
        if s[i] == '0':
            remove[i] = True
            cnt += 1
    s = [s[j] for j in range(len(s)) if not remove[j]]
    t = ''.join(s)
    return t, cnt


cal_cnt = 0
zero_cnt = 0

while int(data) != 1:
    data, cnt = remove_zero(data)
    cal_cnt += 1
    zero_cnt += cnt
    temp = list(bin(len(remove_zero(data)[0]))) # 0을 제거하고 이진수로 변환 (이진수)
    data = ''.join(map(str, temp[2:])) # 0을 제거한 이후의 수 (십진수)


print([cal_cnt, zero_cnt])


"""
# while 반복문 틀린 부분
while int(data) > 1:
    temp = list(bin(len(remove_zero(data)[0])))
    data = ''.join(map(str, temp[2:]))
    cal_cnt += 1
    zero_cnt += remove_zero(data)[1]


print(remove_zero(data))
temp = list(bin(len(remove_zero(data)[0])))
data = ''.join(map(str, temp[2:]))
print(remove_zero(data))
temp = list(bin(len(remove_zero(data)[0])))
data = ''.join(map(str, temp[2:]))
print(remove_zero(data))


# 모범답안
def solution(s):
    a, b = 0, 0
    while s != '1':
        a += 1
        num = s.count('1')
        b += len(s) - num
        s = bin(num)[2:]
    return [a, b]
"""





