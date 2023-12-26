from collections import deque

def bfs(i, j, maps, visited):
    answer = [int(maps[i][j])]
    dist = {0 : [0, 1], 1 : [0, -1], 2 : [1, 0], 3 : [-1, 0]}
    q = deque([(i, j)])
    
    while q:
        y, x = q.popleft()
        
        for i in range(4):
            nx = x + dist[i][0]
            ny = y + dist[i][1]
            
            if 0 <= ny < len(maps) and 0 <= nx < len(maps[0]) and maps[ny][nx] != 'X' and not visited[ny][nx]:
                visited[ny][nx] = True
                answer.append(int(maps[ny][nx]))
                q.append((ny, nx))
    return sum(answer)
        
    

def solution(maps):
    answer = []
    n = len(maps)
    m = len(maps[0])
    visited = [[False] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and maps[i][j] != 'X':
                visited[i][j] = True
                answer.append(bfs(i, j, maps, visited))
            visited[i][j] = True
            
    return sorted(answer) if answer != [] else [-1]