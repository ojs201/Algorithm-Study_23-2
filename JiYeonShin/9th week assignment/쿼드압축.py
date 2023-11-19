result = [0,0]

def solution(arr):
    global result
    result = [0, 0]
    compress(arr, 0, 0, len(arr))
    return result

def compress(arr, start_y, start_x, length):
    global result
    num = arr[start_y][start_x]
    for y in range(start_y, start_y + length):
        for x in range(start_x, start_x + length):
            if(num != arr[y][x]):
                compress(arr, start_y, start_x, length//2)
                compress(arr, start_y, start_x+length//2, length//2)
                compress(arr, start_y+length//2, start_x, length//2)
                compress(arr, start_y+length//2, start_x+length//2, length//2)
                return
    result[num] += 1
    return