class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        right = 0
        prev = nums[right]
        for i in range(1, len(nums)):
            if nums[i] < prev:
                right = i
            else:
                prev = nums[i]
                
        left = len(nums) - 1
        prev = nums[left]
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] > prev:
                left = i
            else:
                prev = nums[i]
        return right - left + 1 if left < right else 0
