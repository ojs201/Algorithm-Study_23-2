import math

def GCD(x, y):
    while (y):
        x,y = y, x % y
    return x


def LCM(x, y):
    result = (x * y) // GCD(x, y)
    return result


arr = list(map(int, input().split()))
result = 0
for i in range(0, len(arr) - 1):
    if i == 0:
        result = LCM(arr[i], arr[i + 1])
    else:
        result = LCM(result, arr[i + 1])

print(result)





