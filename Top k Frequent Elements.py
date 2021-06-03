class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numFreq = {}
        output = []
        for word in nums:
            if word not in numFreq:
                numFreq[word] = 0
            numFreq[word] += 1
        
        numFreq2 = {}
        maxFreq = 0
        for key, val in numFreq.items():
            if val in numFreq2:
                numFreq2[val].append(key)
            else:
                numFreq2[val] = [key]
            maxFreq = max(maxFreq, val)
        
        output = []
        for freq in range(maxFreq, -1, -1):
            if freq in numFreq2:
                output += numFreq2[freq]
            if len(output) >= k:
                return output
            
        return output
