# start에서 레버가는 최소거리 + 레버에서 exit가는 최소거리
# 각각 bfs돌리기, 돌리다가 만약 갈 수 없는 경우가 있다면 -1리턴

from collections import deque

def solution(maps):
    answer = 0
    start = [0, 0]
    lever = [0, 0]
    exit = [0, 0]
    mapArr = [list(map) for map in maps]
    #주어진 MAP돌면서 start, lever, exit 찾아주기
    for y in range(len(mapArr)):
        for x in range(len(mapArr[0])):
            if(mapArr[y][x] == "S"):
                start[0], start[1] = y, x 
            elif(mapArr[y][x] == "L"):
                lever[0], lever[1] = y, x
            elif(mapArr[y][x] == "E"):
                exit[0], exit[1] = y, x
    #출발 -> 레버
    startToLever = bfs(mapArr, start, lever)
    if(startToLever == -1):
        return -1
    #레버 -> 탈출구
    leverToExit = bfs(mapArr, lever, exit)
    if(leverToExit == -1):
        return -1   
    return startToLever + leverToExit

def bfs(mapArr, start, end):
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]
    visit = [[False for _ in range(len(mapArr[0]))] for _ in range(len(mapArr))]
    dq = deque()
    visit[start[0]][start[1]] = True
    dq.append([start[0], start[1], 0])
    while(dq):
        y, x, t = dq.popleft()
        if(y == end[0] and x == end[1]):
            return t
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if(0 <= ny < len(mapArr) and 0 <= nx < len(mapArr[0])):
                if(mapArr[ny][nx] != "X" and visit[ny][nx] == False):
                    visit[ny][nx] = True
                    dq.append([ny, nx, t+1])
    return -1
        
