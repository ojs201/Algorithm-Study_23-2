"""
LV2. 혼자 놀기의 달인
[https://school.programmers.co.kr/learn/courses/30/lessons/131130]

[풀이]
1. 첫번째 카드부터 마지막 카드까지 아래 과정을 반복한다.
    1. 첫 번째 카드부터 열어야 할 카드를 이미 열 때까지 계속 상자를 연다.
    2. 이때 나온 조합이 이전에 나온 경우 무시하고, 처음 나온 조합이면 추가한다.
2. 지금까지 구한 모든 조합을 길이 순으로 정렬하고, 가장 긴 두 조합의 길이를 곱한다.
3. 곱한 값을 반환한다.
"""
def find_groups(cards):
    counts = []    
    
    for idx in range(len(cards)):
        visited = []
        
        while cards[idx] not in visited:
            visited.append(cards[idx])
            idx = cards[idx] - 1
        
        if (visited := sorted(visited)) not in counts:
            counts.append(visited)
        
    return sorted(counts, key=len)


def solution(cards):
    if len(groups := find_groups(cards)) > 1:
        return len(groups[-2]) * len(groups[-1])
    return 0
