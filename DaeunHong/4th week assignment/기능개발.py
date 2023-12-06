# 기능개발

def solution(progresses, speeds):
    day = []
    for i in range(len(progresses)):
        temp = progresses[i]
        dayCnt = 0
        while temp < 100:
            temp += speeds[i]
            dayCnt += 1
        day.append(dayCnt)
    answer = []

    first = day[0]
    count = 1
    for i in range(1, len(day)):
        if first >= day[i]:
            count += 1
        else:
            answer.append(count)
            first = day[i]
            count = 1
    answer.append(count)
    return answer