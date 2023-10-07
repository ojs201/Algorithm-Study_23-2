from collections import Counter

# 나의 풀이 (100/100)

# 풀이방법
# : want와 number를 딕셔너리 형태로 묶어줌. 그러면 품목과 개수 형태가 묶여서 나옴.
# : discount 리스트를 인덱스 0부터 10개의 항목씩 봐야 하므로 for문 조정.
# : my_want와 market을 비교하여 같으면 cnt를 올려줌
# : 비교하기 위해 두 딕셔너리를 key값으로 정렬시킴. (좋은 방법인진 모르겠다)

def solution(want, number, discount):
    
    cnt = 0
    
    my_want = dict(zip(want, number))
    my_want = sorted(my_want.items(), key=lambda x:x[0])
    
    for i in range(len(discount) - sum(number) + 1):
        tmp_li = discount[i:i+10]
        market = Counter(tmp_li)
        market = sorted(market.items(), key=lambda x:x[0])
        
        if my_want == market:
            cnt += 1
    
    return cnt