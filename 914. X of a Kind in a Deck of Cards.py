from collections import Counter
def hasGroupsSizeX(deck):
    counter = Counter(deck)
    minimum = min(counter.values())
    for unit in range(2, minimum + 1):
        flag = True
        for key in counter:
            if counter[key] % unit != 0:
                flag = False
        if flag:
            return True
    return False
