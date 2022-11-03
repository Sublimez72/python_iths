
def solution(x):
    try:
        # Sort the list using the anonymous function lambda and list comprehension.
        x.sort(key=lambda s: [int(i) for i in s.split(".")])

    except Exception as e:
        print(e)

    return x
