from collections import defaultdict

def solution(n, words):
    dict = defaultdict(int)
    round = 0
    for i in range(len(words)):
        if(i != 0):
            if(words[i-1][-1] != words[i][0] or dict[words[i]] != 0): #탈락
                return [i%n+1, i//n+1]
        dict[words[i]] += 1
    return [0, 0]

# 0 => 1 1
# 1 => 2 1
# 2 => 3 1
# 3 => 1 2
# 4 => 2 2
# 5 => 3 2

# 3으로 나눈 나머지에 +1, 3으로 나눈 몫 +1
# 번호 => n으로 나눈 나머지에 +1
# 차례 => n으로 나눈 몫에 +1