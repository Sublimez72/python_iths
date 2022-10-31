

def solution(filename):
    try:
        result = {
            "Shortest word": ["abcdefghijklmnopqrstuvwxyz"],
            "Longest word": [""],
            "How many words": 0,
            "How many lines": 1,
            "How many spaces": 0
            }

        # Counting number of occurences of each letter
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
            # Going back to the start of the file
            f.seek(0)

            # Counting the number of occurences of each word and finding the longest and shortest one
            for lines in f:
                for word in lines.split():
                    if word.endswith("."):
                        word = word[:-1]

                    if len(word) > len(result["Longest word"][0]):
                        result["Longest word"] = []
                        result["Longest word"].append(word)
                    
                    elif len(word) == len(result["Longest word"][0]):
                        result["Longest word"].append(word)

                    if len(word) < len(result["Shortest word"][0]):
                        result["Shortest word"] = []
                        result["Shortest word"].append(word)

                    elif len(word) == len(result["Shortest word"][0]):
                        result["Shortest word"].append(word)
                    
                    result["How many words"] += 1
        # Sorting the list
        result = dict(sorted(result.items()))
        
        # Printing results to terminal
        print(f"Number of lines: \t{result['How many lines']}")
        print("-" * 50)

        print(f"Number of words: \t{result['How many words']}")
        print("-" * 50)

        print(f"Number of spaces: \t{result['How many spaces']}")
        print("-" * 50)

        print("Longest word/words.")
        print("-" * 50)
        for word in result["Longest word"]:
            print(word)
        print()

        print("Shortest word/words")
        print("-" * 50)
        for word in result["Shortest word"]:
            print(word)
        print()


        print("Occurences per letter")
        print("-" * 50)
        for key in result:
            if len(key) == 1:
                print(f"{key}: {result[key]}")

        
        return result
    
    
    except Exception as e:
        print(e)


solution("assignments/assignment-3/minion-submissions/minion-3.txt")

