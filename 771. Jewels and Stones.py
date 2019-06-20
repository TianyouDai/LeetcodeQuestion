def numJewelsInStones(J,S):
    c=0
    for i in J:
        c = c + S.count(i)
    return c
            
        
