class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        way_up = True
        current_i = current_j = 0
        row, col = len(mat), len(mat[0])
        result = [ ]
        while len(result) < row * col:
            result.append(mat[current_i][current_j])
            if way_up:
                if current_i == 0:
                    if current_j == col - 1:
                        current_i += 1
                    else:
                        current_j += 1
                    way_up = False
                elif current_j == col - 1:
                    current_i += 1
                    way_up = False
                else:
                    current_i -= 1
                    current_j += 1
            else:
                if current_i == row - 1:
                    if current_j == 0:
                        current_j += 1
                    else:
                        current_j += 1
                    way_up = True
                elif current_j == 0:
                    current_i += 1
                    way_up = True
                else:
                    current_i += 1
                    current_j -= 1

        return result


print(Solution().findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]])) # [1,2,4,7,5,3,6,8,9]
print(Solution().findDiagonalOrder([[1,2],[3,4]])) # [1,2,3,4]