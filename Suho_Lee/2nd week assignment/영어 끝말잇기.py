# 첫번째 풀이 : 90점

# 이유는 나도 잘 모르겠다...
# elif 쪽에서 코드 구현 문제가 있다.
# 하지만, elif 문에서 answer를 출력하면 제대로 출력되지만, 
# return 했을 때 [0,0]으로 값이 나와 문제가 발생함...

def solution(n, words):
    answer = [0, 0]

    for i in range(1, len(words)):
        if words[i-1][-1] != words[i][0]: # 1) 앞 사람 단어의 마지막 글자로 시작하지 않을 때
            answer = [(i%n)+1 , (i//n)+1]
            break;
        elif words[i-1] in words[i:]: # 2) 말한 단어를 똑같이 말할 때
            for idx in range(i, len(words[i:]) + 1):
                if words[i-1] == words[idx]:
                    answer = [(idx%n)+1 , (idx//n)+1]
                    break;

    return answer



# 두번째 풀이 : 100점
# elif문에서의 인덱싱의 변화를 주어 (탐색 타겟과 범위를 다르게 지정) 코드 구현

def solution(n, words):
    answer = [0, 0]

    for i in range(1, len(words)):
        if words[i-1][-1] != words[i][0]: # 1) 앞 사람 단어의 마지막 글자로 시작하지 않을 때
            answer = [(i%n)+1 , (i//n)+1]
            break;
        elif words[i] in words[:i]: # 2) 말한 단어를 똑같이 말할 때
            answer = [(i%n)+1 , (i//n)+1]
            break;
        else:
            answer = [0,0]

    return answer
