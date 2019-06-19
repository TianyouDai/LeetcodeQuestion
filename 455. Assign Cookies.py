def findContentChildren(g, s):
    if len(s) == 0:
        return 0

    g.sort()
    s.sort()
        
    j = 0
    res = 0

    for i in s:
        if j < len(g) and i >= g[j]:
            j += 1
            res += 1
    return res
