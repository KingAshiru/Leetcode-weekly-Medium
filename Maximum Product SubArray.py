class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = cmin = cmax = nums[0]
        for n in nums[1:]:   
            tempMax = max(n, cmin*n, cmax*n)
            cmin = min(n, cmin*n, cmax*n)
            
            cmax = tempMax
            if cmax > res: 
                res = cmax  
                
        return res
