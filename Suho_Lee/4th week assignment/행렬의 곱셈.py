import numpy as np

# 나의 풀이 (100/100)
# 결국 numpy 라이브러리 도움을 받았다..
def solution(arr1, arr2):
    result = np.dot(arr1, arr2)
    
    # ndarray 형태를 파이썬 list형태로 바꿔주기
    # 안그러면 TypeError: Object of type int64 is not JSON serializable 에러남.
    result = result.tolist()
    
    # print(answer)
    return result
    
    
# 내적 구현하는 정석 풀이
def solution(arr1, arr2):
    
    # 배열 초기화
    answer = [[0]*len(arr2[0]) for _ in range(len(arr1))]
    
    
    for i in range(len(arr1)): 
        lists = []
        for j in range(len(arr2[0])): 
            for k in range(len(arr1[0])): 
                answer[i][j] += arr1[i][k] * arr2[k][j]
                
                
    return answer
    