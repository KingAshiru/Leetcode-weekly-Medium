class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        ones_count = [0, 1]
        
        for i in range(2, num+1):
            
            # look up and compute ones count from subproblem
            cur_ones_count = ones_count[ i & (i-1) ] + 1
            
            # update table
            ones_count.append( cur_ones_count )
        
        
        if num >= 2:
            # general case 
            return ones_count
        
        else:
            # corner case handle
            return ones_count[:num+1]
