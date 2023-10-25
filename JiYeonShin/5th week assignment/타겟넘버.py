def solution(numbers, target):
    answer = dfs(0, target, 0, numbers)
    return answer

def dfs(idx, target, sum, numbers):
    if(idx == len(numbers)):
        if(sum == target):
            return 1
        else:
            return 0
    return dfs(idx+1, target, sum+numbers[idx], numbers) + dfs(idx+1, target, sum-numbers[idx], numbers)
