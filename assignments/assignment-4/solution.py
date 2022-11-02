

def solution(x, y):
    try:
        x_axis = 0
        y_axis = 0
        # calculate value on x axis with y axis 1
        number = 0
        for i in range(1, x + 1):
            number = number + i
            x_axis = number

        # calculate y axis value from variable x_axis
        num = 0
        for i in range(x, y + x):
            y_axis = x_axis + num
            num = num + i

        return str(y_axis)
    except Exception as e:
        print(e)
