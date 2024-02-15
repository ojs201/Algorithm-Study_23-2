# enemy를 순회하면서 만약 상대한 총 enemy의 수가 병사의 수보다 많다진다면,
# 이전 라운드 중에 enemy가 가장 큰 라운드에 무적권을 쓰면 된다.
# 따라서 PriorityQueue를 사용하여 enemy가 가장 많았던 라운드 정보를 기억해둔다.

# 4 2 4 5 3 3 1 예제로 보면

# 4 + 2 < 7 아직 방어 가능
# 4 + 2 + 4 > 7 방어 불가능 -> 앞에 상대했던 라운드 중에 가장 큰 거(4)에 무적권 쓰기 2+4
# 2 + 4 + 5 > 7 방어 불가능 -> 앞에 상대했던 라운드 중에 가장 큰 거(5)에 무적권 쓰기 2+4
# 2 + 4 + 3 > 7 방어 불가능 -> 앞에 상대했던 라운드 중에 가장 큰 거(4)에 무적권 쓰기 2+3 -----------방어권 3개 다씀
#2 + 3 + 3 > 7 방어 불가능 -> 더이상 무적권 없으므로 끝

from queue import PriorityQueue

def solution(n, k, enemy):
    answer = len(enemy)
    enemyNumToFight = 0
    que = PriorityQueue() #큐에 널을 때 - 붙여서 내림차순으로 넣어야한다.
    for i, enemyNum in enumerate(enemy):
        que.put(-enemyNum)
        enemyNumToFight += enemyNum
        if(enemyNumToFight > n): #방어 불가능
            enemyNumToFight += que.get() #무적권을 안 썼던 라운드 중 enemy가 가장 큰거에 무적권을 써야한다!
            k -= 1
            if(k < 0): #무적권 더이상 못씀
                return i   
    return answer