class Solution(object):
    def checkValidCuts(self, n, rectangles):
        """
        :type n: int
        :type rectangles: List[List[int]]
        :rtype: bool
        """

        sorted_rectangles = sorted(rectangles, key=lambda x:x[1])

        lasty = -1
        count = 0
        # Try making two horizontal cuts
        for startx, starty, endx, endy in sorted_rectangles:
            if starty >= lasty:
                count += 1
            lasty = max(lasty, endy)
        if count > 2 :
            return True
        count = 0
        lastx = -1
        sorted_rectangles = sorted(rectangles, key=lambda x:x[0])
        for startx, starty, endx, endy in sorted_rectangles:
            if startx >= lastx:
                count += 1
            lastx = max(lastx, endx)
        if count > 2 :
            return True
        return False


print(Solution().checkValidCuts(5, [[1,0,5,2],[0,2,2,4],[3,2,5,3],[0,4,4,5]])) # True
print(Solution().checkValidCuts(4, [[0,0,1,1],[2,0,3,4],[0,2,2,3],[3,0,4,3]])) # True
print(Solution().checkValidCuts(4,[[0,2,2,4],[1,0,3,2],[2,2,3,4],[3,0,4,2],[3,2,4,4]])) # False