class Solution(object):
    def minMaxDifference(self, num):
        """
        :type num: int
        :rtype: int
        """
        max_num_str = str(num)
        min_num_str = max_num_str
        index = 0
        while index < len(max_num_str)  and max_num_str[index] == '9':
            index += 1
        if index < len(max_num_str):
            max_num_str = max_num_str.replace(max_num_str[index], '9')
        min_num_str = min_num_str.replace(min_num_str[0], '0')
        return int(max_num_str) - int(min_num_str)

print(Solution().minMaxDifference(11891)) # 99009
print(Solution().minMaxDifference(90)) # 99