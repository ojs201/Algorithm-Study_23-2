def solution(sequence, k):
    if not sequence :
        return None
    
    answerlist = []
    start, end = 0, 1
    current_sum = sequence[0]
    
    while True:
        if current_sum == k:
            answerlist.append([start, end - 1])

        if current_sum > k:
            current_sum -= sequence[start]
            start += 1
        else:
            if end < len(sequence):
                current_sum += sequence[end]
                end += 1
            else:
                break

    return sorted(answerlist, key=lambda x: (x[1] - x[0], len(x)))[0]