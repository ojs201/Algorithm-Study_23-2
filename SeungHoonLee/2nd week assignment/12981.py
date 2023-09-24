"""   
LV2. 영어 끝말잇기
[https://school.programmers.co.kr/learn/courses/30/lessons/12981]

풀이:
1. 이전 단어와 현재 단어를 비교한다.
2. 다음 조건을 검사한다.
    2.1. 현재 단어가 이전에 등장했던 경우:
    2.2. 이전 단어의 끝 글자와 현재 단어의 시작이 같은 경우:

3.1. <조건 2>에 만족하는 경우 [번호, 차례]를 반환한다.
3.2. 모든 단어가 <조건 2>가 만족하지 않는 경우 [0, 0]을 반환한다.


[풀이: 반환 값 공식]
1차원 배열을 열의 수 'N'를 가지는 2차원 배열로 변환한다고 가정할때,
1차원 배열의 특정 인덱스 K에 해당하는 2차원 배열의 위치는 다음과 같다.

arr1D[K] = arr2D[K//N][K%N] (이때, K는 열의 수)

e.g.
1차원 배열 arr1D을 열의 개수(N)가 4인 2차원 배열 arr2D로 변환

-> arr1D[12] => arr2D[4][3]

- 만약 K = 5 일때 행은 1(=5/4), 열은 1(=5%4), 즉 arr2D[1][1] == arr1D[5]
- 만약 K = 11 일때 행은 2(=11/4), 열은 3(=11%4), 즉 arr2D[3][2] == arr1D[11]

문제에서 주어진 [번호, 차례]의 경우 번호는 열, 차례는 행에 해당한다.
즉, [번호, 차례] == [열, 행] == [K%N, K//N]
"""
def solution(n, words):
    visited = [words[0]]

    for i in range(1, len(words)):
        prev, word = words[i-1], words[i]
    
        if word in visited or prev[-1] != word[0]:
            return [(i%n) + 1, (i//n) + 1]
        
        visited.append(word)

    return [0, 0]
