class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        space  = []
        space.append(0)
        for i in flowerbed:
            space.append(i)
        space.append(0)

        for j in range(len(flowerbed)):
            if space[j: j + 3] == [0, 0, 0]:
                space[j + 1] = 1
                count = count + 1

        if count >= n:
            return True
        return False
        
