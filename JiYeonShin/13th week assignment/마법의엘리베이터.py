#일의자리 숫자부터 확인
#5보다 크면 10에 가까우니까 +해주기
#5보다 작으면 0에 가까우니까 -해주기
#5면 그 앞자리수에 따라서 100에 가까우면 +, 0에 가까우면 -

def solution(storey):
    answer = 0
    while(storey != 0):
        sware, remain = divmod(storey, 10)
        if remain > 5:
            answer += (10 - remain)
            sware += 1
        elif remain < 5:
            answer += remain
        else:
            if sware % 10 > 4:
                sware += 1
            answer += remain
        storey = sware
    return answer
