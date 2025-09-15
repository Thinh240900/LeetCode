from collections import defaultdict


class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        count = 0
        dict = defaultdict(int)
        for ans in answers:
            if ans == 0:
                count += 1
            else:
                if ans not in dict :
                    dict[ans] = 1
                    count += ans + 1
                else:
                    if dict[ans] < ans +1:
                        dict[ans] += 1
                    else:
                        dict[ans] = 1
                        count += ans + 1

        return count
print(Solution().numRabbits([1,1,2])) # 5
print(Solution().numRabbits([0,0,1,1,1])) # 6
print(Solution().numRabbits([10,10,10])) # 11