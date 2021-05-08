class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # there can only be at most 2 majority elements in an array
        # find those two elements, if exist
        num1, num2 = 0, 0
        count1, count2 = 0, 0
        res = []
        for num in nums: 
            if num == num1:
                count1 += 1
            elif num == num2:
                count2 += 1
            elif count1 == 0:
                num1 = num
                count1 = 1
            elif count2 == 0:
                num2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        # verify if the elements found are the majority numbers
        count1 = 0
        count2 = 0
        for num in nums:
            if num == num1:
                count1 += 1
            elif num == num2:
                count2 += 1
        l = len(nums)
        if count1 > l/3:
            res.append(num1)
        if count2 > l/3:
            res.append(num2)
        return res
