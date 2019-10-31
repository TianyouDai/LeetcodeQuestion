class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        p = []
        for i in range(len(arr)-1):
            p.append([arr[i], arr[i+1]])
        d = dict()
        for x in p:
            t = (x[1]-x[0])
            if t not in d:
                d[t] = []
                d[t].append(x)
            else:
                d[t].append(x)
        return d[min(list(d.keys()))]



        
