def uncommonFromSentences(A, B):
    tempList = A.split(' ') + B.split(' ')
    repeatList = []
    resultLsit = []
        
    for element in tempList:
        if element not in repeatList:
            if element not in resultLsit:
                resultLsit.append(element)
            else:
                resultLsit.remove(element)
                repeatList.append(element)
            
    return(resultLsit)
