# 영어 끝말잇기
# https://school.programmers.co.kr/learn/courses/30/lessons/12981

def solution(n, words):
    def has_duplicates(list):
        return len(list) != len(set(list))

    def has_diff(list):
        for i in range(len(list) - 1):
            if list[i][-1] != list[i + 1][0]:
                return True
                break

    if len(words) % n == 0:
        a = n
    else:
        a = len(words) % n

    b = len(words) // n

    answer = [a, b]

    if has_duplicates(words) == False:
        if has_diff(words) == True:
            if len(words) % n == 0:
                a = n
            else:
                a = len(words) % n
            b = len(words) // n
            answer = [a, b]
        else:
            answer = [0, 0]

    return answer