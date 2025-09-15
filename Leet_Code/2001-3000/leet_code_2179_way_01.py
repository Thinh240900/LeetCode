# class Solution(object):
#     def goodTriplets(self, nums1, nums2):
#         """
#         :type nums1: List[int]
#         :type nums2: List[int]
#         :rtype: int
#         """
#         dict2 = {}
#         result = 0
#         for index, value in enumerate(nums2):
#             dict2[value] = index
#
#
#         dict1 = {}
#         for index, value in enumerate(nums1):
#             for key in dict1.keys():
#                 if dict2.get(key) < dict2.get(value):
#                     dict1[key].append(value)
#             dict1[value] = []
#
#         for key, value in dict1.items():
#             for num in value:
#                 result += len(dict1.get(num))

        # for i in range(len(nums1) - 2):
        #     for j in range(i + 1, len(nums1) - 1):
        #         if dict2.get(nums1[i]) < dict2.get(nums1[j]):
        #             for k in range(j + 1, len(nums1)):
        #                 if dict2.get(nums1[k]) > dict2.get(nums1[j]):
        #                     result += 1
        # return result


class FenwickTree:
    def __init__(self, size):
        self.tree = [0] * (size + 1)

    def update(self, index, delta):
        index += 1
        while index <= len(self.tree) - 1:
            self.tree[index] += delta
            index += index & -index

    def query(self, index):
        index += 1
        res = 0
        while index > 0:
            res += self.tree[index]
            index -= index & -index
        return res

class Solution(object):
    def goodTriplets(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        n = len(nums1)
        pos2, reversedIndexMapping = [0] * n, [0] * n
        for i, num2 in enumerate(nums2):
            pos2[num2] = i
        for i, num1 in enumerate(nums1):
            reversedIndexMapping[pos2[num1]] = i
        tree = FenwickTree(n)
        res = 0
        for value in range(n):
            pos = reversedIndexMapping[value]
            left = tree.query(pos)
            tree.update(pos, 1)
            right = (n - 1 - pos) - (value - left)
            res += left * right
        return res
print(Solution().goodTriplets([2,0,1,3], [0,1,2,3]))
print(Solution().goodTriplets([4,0,1,3,2], [4,1,0,2,3]))