# set함수 이용해서 중복제거

def solution(element):
    answer = []
    elements = element * 2
    
    for i in range(len(element)):
        for j in range(len(element)):
            answer.append(sum(elements[j:j+i+1]))

    answer = len(set(answer))
    return answer