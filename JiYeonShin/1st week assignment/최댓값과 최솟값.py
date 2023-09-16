def solution(s):
    answer = ''
    sortedList = sorted(list(map(int, s.split(" "))))
    answer = str(sortedList[0]) + " " + str(sortedList[-1])
    return answer