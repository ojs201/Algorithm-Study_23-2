def solution(s):
    answer = ''
    words = s.split(" ")
    for i in range(len(words)):
        if(words[i] != ""):
            words[i] = words[i][0].upper() + words[i][1:].lower()
    answer = " ".join(words)
    return answer
