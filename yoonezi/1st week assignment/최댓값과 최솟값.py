# 직접 입력은 받으며 str -> int 변환은 해봤지만, 이미 공백이 포함된 배열을 이용하니
# "어떻게 문자형을 숫자로 바꿔야 하지" 가 가장 큰 문제였음

# map() 을 사용해서 map(int, 배열.split(' ')) 을 사용해보자.

# 문자열을 공백 기준으로 나눠서 리스트 생성 : split()
# str를 int로 전환 : map()
# 정렬 : sort()

def solution(s):
    num = list(map(int, s.split(' ')))
    num.sort()
    answer = str(num[0]) + " " + str(num[-1])
    return answer


# 문제풀이 이후
# 굳이 정렬을 사용하지 않고도, max와 min으로도 간단히 풀 수 있던 문제 