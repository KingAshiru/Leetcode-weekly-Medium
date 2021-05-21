class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        count = 0
        for i in range(len(nums)-2):
            count += self.search_pair(nums, target - nums[i], i)
        return count


    def search_pair(self, nums, target_sum, first):
        count = 0
        left, right = first + 1, len(nums) - 1
        while (left < right):
            if nums[left] + nums[right] < target_sum:  # found the triplet
          # since nums[right] >= nums[left], therefore, we can replace nums[right] by any number between
          # left and right to get a sum less than the target sum
                count += right - left
                left += 1
            else:
                right -= 1  # we need a pair with a smaller sum
        return count
