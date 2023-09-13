def solution(s):
    answer = ""

    # 문자열 분리를 위한 split
    # list안의 원소들을 int형으로 바꾸기 위한 map
    # 정렬 sorted 이후, 최댓값 li[0], 최소값 li[-1] 사용
    li = sorted(list(map(int, s.split(" "))))
    answer += (str(li[0]) + " " + str(li[-1]))

    return answer