class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        smallest_difference = math.inf
        for i in range(len(nums)-2):
            left = i + 1
            right = len(nums) - 1
            while (left < right):
                target_diff = target - nums[i] - nums[left] - nums[right]
                if target_diff == 0:  # we've found a triplet with an exact sum
                    return target - target_diff  # return sum of all the numbers

          # the second part of the following 'if' is to handle the smallest sum when we have more than one solution
                if abs(target_diff) < abs(smallest_difference) or (abs(target_diff) == abs(smallest_difference) and target_diff > smallest_difference):
                    smallest_difference = target_diff  # save the closest and the biggest difference

                if target_diff > 0:
                    left += 1  # we need a triplet with a bigger sum
                else:
                    right -= 1  # we need a triplet with a smaller sum

        return target - smallest_difference
