


from cgitb import reset


def solution(filename):
    result = {
        "Shortest word": "",
        "Longest word": "",
        "How many words": 0,
        "How many lines": 1,
        "How many spaces": 0
        }


    with open(filename) as f:
        for i in f.read():
            
            if i == "\n":
                result["How many lines"] += 1

            elif i == " ":
                result["How many spaces"] += 1

            elif i not in result.keys():
                result[i] = 1

            elif i in result.keys():
                result[i] += 1
        
        f.seek(0)

        for lines in f:
            for word in lines.split():
                if word.endswith("."):
                    word = word[:-1]
                if len(word) > len(result["Longest word"]):
                    result["Longest word"] = word


    


    
    # Sorting the list before returning it
    result = dict(sorted(result.items()))
    return result


print(solution("assignments/assignment-3/minion-submissions/minion-1.txt"))

