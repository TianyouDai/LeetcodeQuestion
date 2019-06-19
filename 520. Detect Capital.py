def detectCapitalUse(word):
    count = 1
    count1 = 1
    count2 = 1
    l = len(word)

    if word[0].isupper() == True:
        for i in range(1, l):
            if word[i].isupper() == True:
                count = count +1
            elif word[i].islower() == True:
                count1 = count1 +1            

    if word[0].isupper() == False:
        for i in range(1, l):
            if word[i].islower() == True:
                count2 = count2 +1

    if (count == l) or (count1 == l) or (count2 == l):
            return True
    return False
