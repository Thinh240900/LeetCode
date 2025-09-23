class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        arr_1 = version1.split('.')
        arr_2 = version2.split('.')
        if int(arr_1[0]) > int(arr_2[0]):
            return 1
        if int(arr_1[0]) < int(arr_2[0]):
            return -1

        index_1 = 1
        index_2 = 1
        while index_1 < len(arr_1) and index_2 < len(arr_2):
            result = self.check_minor_version(arr_1[index_1], arr_2[index_2])
            if result!= 0:
                return result
            index_1 += 1
            index_2 += 1
        while index_1 < len(arr_1):
            result = self.check_minor_version(arr_1[index_1], '0')
            if result!= 0:
                return result
            index_1 += 1
        while index_2 < len(arr_2):
            result = self.check_minor_version('0', arr_2[index_2])
            if result!= 0:
                return result
            index_2 += 1
        return 0


    def check_minor_version(self, arr_1, arr_2):
        a = int(arr_1)
        b = int(arr_2)
        if a > b:
            return 1
        if a < b:
            return -1
        return 0


    # def check_minor_version(self, arr_1, arr_2):
    #
    #         minor_version_1 = arr_1.lstrip('0')
    #         minor_version_2 = arr_2.lstrip('0')
    #         n = len(minor_version_1)
    #         m = len(minor_version_2)
    #         i = 0
    #         while i < n and i < m:
    #             if minor_version_1[i] > minor_version_2[i]:
    #                 return 1
    #             if minor_version_1[i] < minor_version_2[i]:
    #                 return -1
    #             i += 1
    #         if i < n:
    #             return 1
    #         if i < m:
    #             return -1
    #         return 0




print(Solution().compareVersion('1.2', '1.10'))
print(Solution().compareVersion('1.01', '1.001'))
print(Solution().compareVersion('1.0', '1.0.0.0'))

