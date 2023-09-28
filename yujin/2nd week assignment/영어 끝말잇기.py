def solution(n,words):
    repeat = [words[0]]
    for i in range(1,len(words)): # +1 하지 않아도 됨
        if words[i][0] == words[i-1][-1] and words[i] not in repeat:
            repeat.append(words[i])
        else:
            return [(i%n)+1, (i//n)+1]
    return [0, 0]