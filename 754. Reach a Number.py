class Solution:
    def reachNumber(self, target: int) -> int:
        move = 0
        target = abs(target)
        
        
        while True:
            _sum = (move + 1) * move/2
            if (_sum + target) % 2 == 0 and _sum >= target:
                return move
            
            move += 1
                
