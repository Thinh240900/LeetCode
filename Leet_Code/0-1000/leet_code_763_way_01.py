class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        last_index = {c: i for i, c in enumerate(s)}
        partitions = []
        count = 0
        last_index_partition = -1
        for i, c in enumerate(s):
            count += 1
            if last_index[c] > last_index_partition:
                last_index_partition = last_index[c]
            if last_index_partition == i :
                partitions.append(count)
                count = 0
        return partitions




print(Solution().partitionLabels("ababcbacadefegdehijhklij")) # [9, 7, 8]
print(Solution().partitionLabels("eccbbbbdec")) # [10]