# 배열을 순회하며 if i의 마지막 글자 == i+1의 마지막 글자면 넘어가고,
# else, 만약 3명이서 하고 9번의 말이 나왔을때 8번째에서 탈락이면
# 2번이 3번째때 탈락

## 반복문을 하나만 써서 풀 수 있지 않을까?
# 더 생각해보기

def solution(n, words):
    answer = [0, 0]
    for i in range(len(words) - 1):
        if words[i][-1] != words[i+1][0]:
            answer = [((i+1) % n) + 1, ((i+1) // n) + 1]
            break

    for i in range(len(words)):
        for j in range(i+1, len(words)):
            if words[i] == words[j]:            
                answer = [ (j % n) + 1, (j // n) + 1]

    return answer

# ------------------------------

def solution(n, words):
    
    for i in range(1, len(words)):
        #글자가 맞지 않을 때
        if words[i][0] != words[i-1][-1] or words[i] in words[:i]:
            return [(i%n)+1, (i//n)+1]
    
    return [0,0]