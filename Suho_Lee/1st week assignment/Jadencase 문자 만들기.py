# 나의 풀이 테스트케이스 8 실패

# def solution(s):
#     answer = ''
    
#     words = s.split(" ")
#     for word in words:
#         answer += (word.capitalize()+" ")
    
#     return answer.rstrip()

def solution(s):
    answer = []
    
    words = s.split(" ")
    for word in words:
        if word: # 문자열이라면
            answer.append(word[0].upper() + word[1:].lower())
        else: #문자열 아니고, 공백이면
            answer.append(word)
    
    return " ".join(answer)