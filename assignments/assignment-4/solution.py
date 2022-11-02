import numpy as np


# Function for creating arrays.
# Pass in the index of an array and it will calculate all the values for the next index.
def create_array(x):
    try:
        num = 0
        counter = x + 1

        for i in arr[x]:

            arr[x + 1, num] = i + counter

            counter = counter + 1
            num = num + 1
    except Exception as e:
        print(e)


def solution(x, y):
    try:
        global arr
        # I was having a problem where numpy was printing all numbers in scientific notation
        # and this line solved it.
        np.set_printoptions(suppress=True)
        # square root of 100_000 rounded up
        side = 320
        arr = np.zeros((side, side))

        # array 0
        number = 0
        for i in np.arange(1, side + 1):

            number = number + i
            arr[0, i - 1] = number

        # all other arrays
        for i in np.arange(side - 1):
            create_array(i)

        return str(int(arr[y-1, x-1]))
        
    except Exception as e:
        print(e)
