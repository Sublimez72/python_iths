
def solution(x):
    try:
        # Sort the list using the anonymous function lambda and list comprehension.
        x.sort(key=lambda s: [int(i) for i in s.split(".")])
    
    # Generic exception since we don't want to print anything to the terminal
    except Exception as e:
        pass

    return x


