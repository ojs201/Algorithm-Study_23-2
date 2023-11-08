dict = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

def change_10_to_n(number, n): #number를 n진수로 바꾸기
    answer = 0
    base = ''
    while number > 0:
        number, remain = divmod(number, n)
        base = dict[remain] + base
    return base

def solution(n, t, m, p):
    answer = ''
    answerSheet = '0'
    number = 1
    while(len(answerSheet) < m*(t-1)+p):
        answerSheet += change_10_to_n(number, n)
        number += 1
    for i in range(t):
        answer += answerSheet[m*(i)+p-1]
    return answer