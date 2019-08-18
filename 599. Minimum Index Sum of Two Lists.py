class Solution(object):
	def findRestaurant(self, list1, list2):
		l1 = set(list1)
		l2 = set(list2)
		c = l1&l2
        
		res = []
		minL = 1 + len(list1) + len(list2)
		for x in c:
			totalL = list1.index(x) + list2.index(x)
			if totalL < minL:
				res = []
				res.append(x)
				minL = totalL
			elif totalL == minL:
				res.append(x)
    
		return res
