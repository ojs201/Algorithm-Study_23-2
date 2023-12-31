#미리 0으로 초기화한 틀을 만들어 주고 그 후 채워주는 방식으로 풀었다.

#n=6일 경우 아래와 같이 채워진다.
#[1,2,3,4,5,6] -> [7,8,9,10,11] -> [12,13,14,15] -> [16,17,18] -> [19,20] -> [21]

#방향은 아래, 오른쪽, 위 3가지이므로 3으로 나눈 나머지에 따라 방향 결정
# 3으로 나누었을 때, 나머지 0 => 아래
#                  나머지 1 => 오른쪽
#                  나머지 2 => 위


dir = [[1,0], [0,1], [-1,-1]] #아래, 오른쪽, 위

def solution(n):
    answer = [[0] * i for i in range(1, n+1)]
    y, x = -1, 0
    now = 1
    for i in range(n):
        for _ in range(n-i):
            dir_y, dir_x = dir[i%3]
            y, x = y + dir_y, x + dir_x
            answer[y][x] = now
            now += 1
    return sum(answer, [])


