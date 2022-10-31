

def solution(s):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    # Create the translation table
    trans = str.maketrans(alphabet, alphabet[::-1] , " ")
    result = ""
    # Iterate through the string
    for letter in s:
        # if the letter is lowercase we translate it using our translation table
        if letter.islower():
            result += letter.translate(trans)
        else:
            result += letter
    
    
    return result

