def sortArrayByParity(A):
    lis = []
    lisOdd = []
    for i in range(len(A)):
        if A[i] % 2 == 0:
            lis.append(A[i])
        else:
            lisOdd.append(A[i])
        
    for j in range(len(lisOdd)):
        lis.append(lisOdd[j])
        
    return lis
                
