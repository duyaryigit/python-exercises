def PalindromeTwo(strParam):
    
    punctation = "-*.,;^+%&"
    without_spaces = strParam.replace(" ", "").lower()
    without_punc = ""

    for i in without_spaces:
        if i in punctation:
            continue
        else:
            without_punc += i
        
    return without_punc == without_punc[::-1]

print(PalindromeTwo(strParam))
