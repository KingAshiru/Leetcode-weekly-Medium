class Solution(object):
    def checkArithmeticSubarrays(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: List[int]
        :type r: List[int]
        :rtype: List[bool]
        """
        output = []
        check = []
        i = 0
        while i < len(l):
            flag = True
            check[:] = nums[l[i]:r[i]+1]
            check.sort()
            diff = check[1] - check[0]
            for j in range(1, len(check)):
                if check[j] - check[j - 1] != diff:
                    flag = False
                    break
            output.append(flag)
            i += 1
        return output
