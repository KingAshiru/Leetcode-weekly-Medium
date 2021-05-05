class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last_head, length = 0, 0
        insert_pos = 0
        
        for i, cur in enumerate(nums):
            if i == 0:                
                last_head = cur
                length = 1
                insert_pos += 1
            else:
                if cur == last_head:
                    if length < 2:
                        length += 1
                        nums[insert_pos] = cur
                        insert_pos += 1
                    else:
                        length += 1   
                else:
                    length = 1
                    last_head = cur
                    nums[insert_pos] = cur
                    insert_pos += 1
                    
        return insert_pos
        
