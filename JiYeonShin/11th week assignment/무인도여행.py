#answer에다가 섬에서 머물 수 있는 날짜 넣고, 마지막에 오름차순 정렬 후 리턴
#map 전체를 돌면서 섬 발견 -> 그 섬을 시작으로 bfs돌면서 day(머물 수 있는 날짜) 계산 -> answer에 추가
from collections import deque

def solution(maps):
    answer = []
    map = [list(i) for i in maps]
    for y in range(len(map)):
        for x in range(len(map[0])):
            if(map[y][x] != "X"): #섬 발견
                answer.append(getDayByBfs(map, y, x))
                
    if(len(answer) == 0):
        answer.append(-1)
    else:
        answer.sort()
    return answer

dir = [(-1,0), (1,0), (0,-1), (0,1)] #상하좌우

def getDayByBfs(map, start_y, start_x):
    day = int(map[start_y][start_x])
    map[start_y][start_x] = "X"
    dq = deque()
    dq.append((start_y, start_x))
    while(dq):
        y, x = dq.popleft()
        for i in range(4):
            ny = y + dir[i][0]
            nx = x + dir[i][1]
            if(0 <= ny < len(map) and 0 <= nx < len(map[0]) and map[ny][nx] != "X"):
                day += int(map[ny][nx]) #날짜 갱신
                map[ny][nx] = "X" #방문 표시
                dq.append((ny, nx))
    return day