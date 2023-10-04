# 멀리 뛰기
# https://school.programmers.co.kr/learn/courses/30/lessons/12914

n = int(input())

data = [0] * (n + 1)
data[0], data[1] = 1, 2

for i in range(2, n):
    data[i] = data[i - 2] + data[i - 1]

print(data[n - 1] % 1234567)