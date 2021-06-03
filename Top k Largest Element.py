class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        freqMap = {}
        for num in nums:
            if num not in freqMap:
                freqMap[num] = 0
            freqMap[num] += 1
        
        count = 0
        while freqMap:
            maxNum = max(freqMap.keys())
            freq = freqMap[maxNum]
            count += freq
            if count >= k:
                return maxNum
            del freqMap[maxNum]
        
