answer = -1
visit = []
d = []

def solution(k, dungeons):
    global visit
    visit = [False for _ in range(len(dungeons))]
    dfs(dungeons, k)
    return answer

def getNumberOfDungeonsToExplore(k, dungeons):
    cnt = 0
    for dungeon in dungeons:
        if(k >= dungeon[0]):
            cnt += 1
            k -= dungeon[1]
    return cnt

def dfs(dungeons, k):
    global answer
    if(len(d)==len(dungeons)):
        answer = max(answer, getNumberOfDungeonsToExplore(k, d))
        return
    for i in range(len(dungeons)):
        if(visit[i] == False):
            visit[i] = True
            d.append(dungeons[i])
            dfs(dungeons, k)
            visit[i] = False
            d.pop()
    
        