from itertools import product
def solution(word):
    vowel = []
    for i in range(1,6):
        for j in product(["A","E","I","O","U"],repeat=i):
            vowel.append("".join(list(j)))
    vowel.sort()
    return vowel.index(word)+1