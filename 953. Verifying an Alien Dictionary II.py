class Solution:  
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        words2 = sorted(words, key=lambda word: self.value(word, order))
        return words == words2
    
    def value(self, words, order):
        return [order.find(x) for x in words]
