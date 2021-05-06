class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        start = 0
        sums = 0
        minCount = float("inf")
        for end in range(len(nums)):
            sums += nums[end]
            count += 1
            while sums >= target:
                minCount = min(minCount, count)
                sums -= nums[start]
                count -= 1
                start += 1
                
        if minCount == float("inf"):
            return 0
        return minCount
                
