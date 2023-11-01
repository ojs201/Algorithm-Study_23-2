from collections import defaultdict

def solution(msg):
    answer = []
    #사전 초기화
    dict = defaultdict(int)
    for i in range(65, 91):
        dict[chr(i)] = i-64
    #그 외 LZW 압축 과정
    word = ""
    for w in msg:
        word += w
        if(word not in dict):
            answer.append(dict[word[:-1]])
            dict[word] = len(dict)+1
            word = word[-1]
    answer.append(dict[word])
    return answer