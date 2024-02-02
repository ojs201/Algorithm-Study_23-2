# 로봇위치를 찾는다.
# 로봇위치 부터 시작해서 상하좌우로 미끄러진다.
# 최소움직임이기 때문에 bfs로 풀어준다.
# 만약 미끄러진 자리가 처음 방문한 곳이라면 
#     현재 위치에 도달하는데 걸리는 최소 수 + 1 로 갱신해준다.
# 이미 방문했던 곳이라면 이미 그 자리에 도달하는 최소 수가 정해진 것이므로 pass한다.
# "G"라면 목표위치에 도달한 것이므로 return (현재 위치에 도달하는데 걸리는 최소 수 + 1)


from collections import deque

def solution(board):
    answer = 0
    board = [list(i) for i in board]
    for y in range(len(board)):
        for x in range(len(board[0])):
            if(board[y][x] == 'R'):
                answer = bfs(board, y, x)
    return answer

dy = [0,0,1,-1]
dx = [1,-1,0,0]

def bfs(board, start_y, start_x):
    board[start_y][start_x] = 0
    dq = deque()
    dq.append((start_y, start_x))
    while(dq):
        y, x = dq.popleft()
        for i in range(4):
            ny, nx = y, x
            while(0 <= ny < len(board) and
                  0 <= nx < len(board[0]) and 
                  board[ny][nx] != 'D'): #벽 OR D("장애물") 만날 때까지 이동
                ny += dy[i]
                nx += dx[i]
            ny -= dy[i] #한 칸 빽 => 벽이나 장애물에 부딫혔을 때 멈추는 곳
            nx -= dx[i]
            if(board[ny][nx] == 'G'): 
                return board[y][x] + 1
            if(board[ny][nx] == '.'):
                board[ny][nx] = board[y][x] + 1
                dq.append((ny, nx))
    return -1
