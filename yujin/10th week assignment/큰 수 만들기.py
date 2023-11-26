def solution(number, k):
    stack = []
    for num in number:
        while k >0 and stack and stack[-1]<num:  # k가 왜 중요한 지 모르겠다
            stack.pop()
            k -= 1
        stack.append(num)
    return "".join(stack[:len(stack) - k])