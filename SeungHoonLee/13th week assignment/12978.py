"""
LV2. 배달
[https://school.programmers.co.kr/learn/courses/30/lessons/12978]

[풀이]
1. 다익스트라 알고리즘을 이용해 [1번] 마을을 다른 마을에 대한 최단 경로를 구한다.
    - 이때 마을 간의 연결된 상태는 양방향 간선이 연결된 것과 동일하기 때문에 이에 대한 전처리가 필요.
2. K 이하의 최단 경로를 가지는 마을의 개수를 센다.
3. <2> 결과를 반환한다.
"""

import heapq

INF = int(1e9)


def solution2(N, road, K):
    """
    heap queue 사용 X 다익스트라 알고리즘 구현
    """
    graph = [[] for _ in range(N + 1)]
    distance = [INF] * (N + 1)

    for a, b, c in road:
        graph[a].append((b, c))
        graph[b].append((a, c))

    q = [(1, 0)]
    distance[1] = 0

    while q:
        now, dist = q.pop(0)

        for adj_node, adj_dist in graph[now]:
            cost = dist + adj_dist

            if cost < distance[adj_node]:
                distance[adj_node] = cost
                q.append((adj_node, cost))

    return len([dist for dist in distance if dist != INF and dist <= K])


def solution(N, road, K):
    graph = [[] for _ in range(N + 1)]
    distance = [INF] * (N + 1)

    for info in road:
        a, b, c = info
        graph[a].append((b, c))
        graph[b].append((a, c))

    def dijkstra(start):
        q = []
        heapq.heappush(q, (0, start))
        distance[start] = 0

        while q:
            dist, now = heapq.heappop(q)

            if distance[now] < dist:
                continue

            for to, cost in graph[now]:
                cost_total = dist + cost

                if cost_total < distance[to]:
                    distance[to] = cost_total
                    heapq.heappush(q, (cost_total, to))

    dijkstra(1)
    return len([dist for dist in distance if dist != INF and dist <= K])
