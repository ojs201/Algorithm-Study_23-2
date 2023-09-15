def solution(s):
    lst = list(map(int,s.split( )))
    lst.sort()
    answer = f"{lst[0]} {lst[-1]}"
    return answer