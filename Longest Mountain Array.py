class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        i = 1
        longest = 0
        
        while i < len(arr) - 1:
            is_peak = arr[i-1] < arr[i] and arr[i] > arr[i+1]
            if not is_peak:
                i += 1
                continue
            left_idx = i - 2
            while left_idx >= 0 and arr[left_idx] < arr[left_idx + 1]:
                left_idx -= 1
            right_idx = i + 2
            while right_idx < len(arr) and arr[right_idx - 1] > arr[right_idx]:
                right_idx += 1
            
            longest = max(longest, right_idx - left_idx - 1)
            i = right_idx
        
        return longest
