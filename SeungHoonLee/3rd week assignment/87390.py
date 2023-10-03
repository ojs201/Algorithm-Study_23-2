"""
LV2. n^2 배열 자르기
[https://school.programmers.co.kr/learn/courses/30/lessons/87390]

- 첫 시도 방법은 주어진 LEFT, RIGHT를 이용해 완전한 리스트를 만들고 slicing 하는 방식으로 품.
- 그러나 시간제한에 걸림, 따라서 전체 리스트를 만드는 것이 아닌, 주어진 범위 내에서만 배열을 생성하는 방식을 고민함

풀이:
- 2차원 배열에 대해 다음과 같은 식이 성립.
    - 2차원 배열 Arr의 행 인덱스 i와 열 인덱스 j에 대해:

        - Arr[i][j] = i + 1 (if i >= j)
        - Arr[i][j] = j + 1 (if i < j)

    - 위 두 식을 정리하면 아래와 같다.

        - Arr[i][j] = max(i, j) + 1

- 따라서 주어진 범위[start, end]에 대해 1차원 인덱스 -> 2차원 행과 열 인덱스로 변환 후, 위 공식을
  적용하면 문제를 해결할 수 있다.
"""


def solution(n, left, right):
    return [max(i // n, i % n) + 1 for i in range(left, right + 1)]
