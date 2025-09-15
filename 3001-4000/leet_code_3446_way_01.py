class Solution(object):
    def sortMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        arr = []
        n = len(grid)
        for i in range((n-1)*2-1):
            j = 0 if i < (n-1) else i - (n-2)
            row = i
            if j != 0 :
                row = 0
            temp = []
            while row < n and j < n:
                temp.append(grid[row][j])
                row += 1
                j += 1
            arr.append(temp)

        for i in range(len(arr)):
            if i < n-1:
                arr[i].sort(reverse=True)
            else:
                arr[i].sort()

        flattened = [x for sublist in arr for x in sublist]
        count = 0
        for i in range((n-1)*2-1):
            j = 0 if i < (n-1) else i - (n-2)
            row = i
            if j != 0 :
                row = 0
            while row < n and j < n:
                grid[row][j] = flattened[count]
                row += 1
                j += 1
                count += 1

        return grid




print(Solution().sortMatrix([[1,7,3],[9,8,2],[4,5,6]])) # [[8,2,3],[9,6,7],[4,5,1]]
print(Solution().sortMatrix([[0,1],[1,2]])) # [[2,1],[1,0]]
print(Solution().sortMatrix([[1]])) # [[1]]