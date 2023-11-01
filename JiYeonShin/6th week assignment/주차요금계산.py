from collections import defaultdict

def getMinutesFromTime(time):
    time = time.split(":")
    return 60*int(time[0]) + int(time[1])

def calFeeFromMinutes(fees, minutes):
    minutes -= fees[0]
    if(minutes <= 0): #기본요금일 경우
        return fees[1]    
    share, remain = divmod(minutes, fees[2]) #추가요금 계산
    if(remain == 0):
        return fees[1] + share*fees[3]
    else:
        return fees[1] + (share+1)*fees[3]
    
def solution(fees, records):
    answer = []
    minutesTable = defaultdict(int)
    inCar = {}
    for record in records:
        record = record.split(" ")
        if(record[2] == "IN"): #입차
            inCar[record[1]] = getMinutesFromTime(record[0])
        else: #출차
            minutes = getMinutesFromTime(record[0]) - inCar[record[1]]
            minutesTable[record[1]] += minutes
            del inCar[record[1]]
    #출차되지 않은 거 처리
    for carNum, inMin in inCar.items():
        minutes = (60*23 + 59) - inMin
        minutesTable[carNum] += minutes
    sortedMinutesTable = sorted(minutesTable.items(), key = lambda x : x[0])
    for carNum, totalMin in sortedMinutesTable:
        answer.append(calFeeFromMinutes(fees, totalMin))
    return answer

# 우선 분 계산을 어떻게 할 것인가 => 분으로 계산해서 계산
# 입차 : 5시 34분 => 5*60 + 34 = 334분
# 출차 : 22시 59분 => 22*60 + 59 = 1379분
# 출차된 내역이 없다면 23시 59분 => 23*60 + 59분으로 계산하기

#inCar에 분 저장해놓고 출차일 경우 분 계산해서 minuteTable에 추가
#inCar에 남아있는거 11:59로 계산해서 minuteTable에 추가
#minuteTable을 돌리면서 주차요금 계산
