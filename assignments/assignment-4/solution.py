

def solution(x, y):

    arr = []
    new_arr = []
    # square root of 100_000 rounded up
    side = 320
    # array on x axis with y axis 1
    number = 0
    for i in range(1, side + 1):
        number = number + i
        arr.append(number)
    # only calculate y axis array for the speciefied x value.
    num = 0
    for i in range(x, side):
        new_arr.append(arr[x-1] + num)
        num = num + i

    result = str(new_arr[y-1])
    return result
