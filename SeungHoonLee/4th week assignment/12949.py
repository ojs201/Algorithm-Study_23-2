"""
LV2. 행렬의 곱셈
[https://school.programmers.co.kr/learn/courses/30/lessons/12949]

풀이:
- 행렬 A, B가 존재하고, A의 열의 수를 `N`이라고 할 때 행렬 A, B의 곱 C에 대해 다음 공식이 성립:
- C[i][j] = Σ_{k=0}^N A[i][k]*B[k][j]
"""


def solution(arr1, arr2):
    answer = []

    for arr1_col in arr1:
        k_arr = []
        for arr2_row in zip(*arr2):
            k_arr.append(sum([el1 * el2 for el1, el2 in zip(arr1_col, arr2_row)]))
        answer.append(k_arr)

    return answer
