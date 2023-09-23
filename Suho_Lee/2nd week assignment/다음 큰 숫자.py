def solution(n):
    # 매개변수로 주어진 n의 2진수 변환 시 1의 개수를 변수로 저장
    target = bin(n)[2:].count('1') 
    
    while True:
        n += 1 # 1씩 증가시키면서 체크
        
        # 만약 증가된 n의 2진수 변환시 1의 개수가 target과 같다면 그 수 return
        if bin(n)[2:].count('1') == target:
            return n