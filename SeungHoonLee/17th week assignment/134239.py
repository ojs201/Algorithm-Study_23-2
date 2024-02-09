"""
LV2. 우박수열 정적분
[https://school.programmers.co.kr/learn/courses/30/lessons/134239]


각 구간 [a, b]에 대한 넓이 == 사다리 꼴 넓이
: (윗변 + 아랫변) * 높이 / 2 

e.g. n=5, numbers = [5, 16, 8, 4, 2, 1]
- [0, 0] = 0
- [0, 1] = (5 + 16) * 1 / 2 = 10.5
- [0, 2] = (16 + 8) * 1 / 2 + 10.5 = 22.5
- ...
- [0, n] = (numbers[n-1] + numbers[n]) + f(n-1)

이때, 주어진 ranges에 대하여:
- [2,-3] => f(n-3) - f(2) => f(2) - f(2) = 0.0
- [0, -1] => f(n-1) - f(0) => f(4) - 0 = 31.5
"""
def area(upper_side, lower_side):
    return (upper_side + lower_side) / 2


def solution(k, ranges):
    numbers = [k]
    
    while k > 1:
        if k % 2 == 0:
            k //= 2
        else:
            k = k * 3 + 1
        numbers.append(k)
    
    areas = [0]
    for i in range(len(numbers)-1):
        areas.append(areas[-1] + area(numbers[i], numbers[i+1]))
        
    answer = []
    n = len(numbers) - 1
    
    for x, y in ranges:
        y += n
        
        if x > y:
            answer.append(-1.0)
        else:
            answer.append(areas[y] - areas[x])
    
    return answer
