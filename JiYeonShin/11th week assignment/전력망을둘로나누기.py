#===풀이 아이디어===
#전선을 하나씩 끊어보며 두 전력망의 송전탑 개수의 차이를 계산 -> 만약 최소값이면 갱신

#===송전탑 개수 차이 계산 방법===
#처음에 하나의 트리 형태로 이루어져있기 때문에, 전선을 끊을 경우 두개의 트리로 나누어지는데, 하나는 무조건 1번 송전탑과 연결되어 있다. 이 개수로 차이를 구할 수 있다.

    # 송전탑 개수 차이 = (1번 송전탑과 연결된 개수 - 나머지 개수)의 절대값
    # 나머지 개수는 n - 1번 송전탑과 연결된 개수과 같으므로
    # 즉, 송전탑 개수 차이 = 2*1번 송전탑과 연결된 개수 - n이다.


from collections import deque

def getDifference(n, graph):
    visit = [False for _ in range(n+1)]
    dq = deque()
    #송전탑 1번과 연결된 개수 구하기
    cnt = 1
    visit[1] = True
    dq.append(1)
    while(dq):
        top = dq.popleft()
        for i in graph[top]:
            if(visit[i] == False):
                visit[i] = True
                dq.append(i)
                cnt += 1
    return abs(2*cnt - n)
    
def solution(n, wires):
    answer = n
    for i in wires: #전선을 하나씩 끊은 graph만들기
        graph = [[] for _ in range(n+1)]
        for j in wires:
            if(i != j):
                x, y = j[0], j[1]
                graph[x].append(y)
                graph[y].append(x)
        diff = getDifference(n, graph) #해당 그래프로 송전탑 차이 계산
        answer = min(answer, diff) #최소일 경우 갱신
    return answer