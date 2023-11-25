def solution(numbers):
    answer = []
    def cal(n):
        last = (~n) & (n+1)
        return (n|last) & ~(last>>1)        

    for n in numbers:
        if n%2 == 0 :
            answer.append(n+1)
        else: 
            tmp = cal(n)
            answer.append(tmp)
    return answer