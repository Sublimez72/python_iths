
def solution(x):
    try:
        x.sort(key=lambda s: [int(i) for i in s.split(".")])
    
    except Exception as e:
        pass


    return x


