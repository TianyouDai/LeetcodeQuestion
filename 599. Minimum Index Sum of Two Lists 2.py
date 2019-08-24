import heapq

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        
        # dict will store all terms in list2
        # and map them to their indexes
        list2_dict = {}
        for i, v in enumerate(list2):
            list2_dict[v] = i
        
        # heap will store an ordered list of
        # index sum for all matching terms
        heap = []
        
        # for each word in list1, we look for a matching
        # word and get the total index sum
        for index, word in enumerate(list1):                            
            
            if word in list2_dict:
                match = [index + list2_dict[word], word]                
                heapq.heappush(heap, match)
        
        # init prev_value to the first value in the heap
        prev_value = heap[0][0]
        
        # collect the answer which is all 
        # matches with the same lowest value
        ans = []
        for value, word in heap:
            
            # while value is the same as the previous
            # collect the answer
            if prev_value == value:
                ans.append(word)
                prev_value = value
            else:
                break
                
        return ans
