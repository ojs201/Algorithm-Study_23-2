#앞에서부터 수를 확인하면서 해당 수를 제거할지 말지 결정
#어떤수를 제거햐냐? 현재 제거해야 할 수가 k라고 할때,
    #해당수가 해당 수 뒤에 있는 k개의 숫자들보다 모두 크다면 제거x => answer에 추가
    #else: 제거o => k - 1 시키기

#어려웠던 부분:해당 수가 9인 경우
#해당 수가 9일 경우는 무조건 뒤에 있는 수들 보다 크다. 
#따라서 검사할 필요 없이 바로 answer에 추가해서 시간복잡도를 줄여라!


def solution(number, k):
    answer = ''
    numbers = list(number)
    for i in range(len(numbers)):
        if(len(numbers)-i == k):
            break
        if(numbers[i] == '9'):
            answer += numbers[i]
            continue
        for j in range(i+1, i+1+k):
            if(numbers[i] < numbers[j]):
                k -= 1
                break
        else:
             answer += numbers[i]
    return answer