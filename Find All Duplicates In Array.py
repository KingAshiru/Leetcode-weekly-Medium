class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for i in range(len(nums)):
            val = abs(nums[i]) - 1
            if nums[val] < 0:
                ans.append(val + 1)
            else:
                nums[val] = -nums[val]
        return ans
