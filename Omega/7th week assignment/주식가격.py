def solution(prices):
    answer = [0] * len(prices)
    stack = []
    for i, price in enumerate(prices):
        while stack and price < prices[stack[-1]]:
            j = stack.pop()
        answer[j] = i - j
        stack.append(i)

          # for문 이후 Stack에남아있는값들 pop
        while stack:
            j = stack.pop()
        answer[j] = len(prices)-1-j

        return answer


