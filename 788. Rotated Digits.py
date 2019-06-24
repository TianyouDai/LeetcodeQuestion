def rotatedDigits(N):
    good_count = 0
    invalid_no = ['3', '4', '7']
    valid_same = ['0', '1', '8']
    valid_diff = ['2', '5', '6', '9']
    for i in range(1,N+1):
        same_count = 0
        diff_count = 0
        invalid = False
        for j in str(i):
            if j in invalid_no:
                invalid = True
            elif j in valid_same:
                same_count += 1
            elif j in valid_diff:
                diff_count += 1
        
        if diff_count == 0:
            invalid = True
        if invalid:
            continue
        else:
            good_count += 1
                    
    return good_count
        
        
