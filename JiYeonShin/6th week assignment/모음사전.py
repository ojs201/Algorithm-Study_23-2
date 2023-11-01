def solution(word):
    answer = 0
    dict = {'A':0, 'E':1, 'I':2, 'O':3, 'U':4}
    for i, w in enumerate(word):
        answer += ((5**(5-i)-1)/4)*dict[w]+1
    return answer