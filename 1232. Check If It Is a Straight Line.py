class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) <= 2:
            return True

        for i in range(2, len(coordinates)):
            x1, y1 = coordinates[i]
            x2, y2 = coordinates[i-1]
            x3, y3 = coordinates[i-2]

            a = x1 * (y2 - y3)
            b = x2 * (y3 - y1)
            c = x3 * (y1 - y2)

            if (a + b + c) / 2 != 0:
                return False
        return True
        
