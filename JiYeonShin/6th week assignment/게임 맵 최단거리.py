from collections import deque

def solution(maps):
    row = len(maps)
    col = len(maps[0])
    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]
    dq = deque()
    dq.append((0,0,1))
    maps[0][0] = 2
    while(dq):
        y, x, t = dq.popleft()
        if(y == row-1 and x == col-1): #도착 
            return t
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if(0 <= ny < row and 0 <= nx < col):
                if(maps[ny][nx] == 1):
                    maps[ny][nx] = 2
                    dq.append((ny, nx, t+1))
    return -1