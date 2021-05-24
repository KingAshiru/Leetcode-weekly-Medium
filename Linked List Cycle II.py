# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return None
        hasCycle = None
        slow = fast = head
        while fast.next and fast.next.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                hasCycle = True
                break
        if not hasCycle:
            return None        
        
        def cycleLength(slow1):
            cur = slow1
            cyLength = 0
            while True:
                cur = cur.next
                cyLength += 1
                if cur == slow1:
                    break
            return cyLength
        
        length = cycleLength(slow)
        ptr1 = ptr2 = head
        
        while length > 0:
            ptr2 = ptr2.next
            length -= 1
        
        pos = 0
        while ptr1 != ptr2:
            ptr1, ptr2 = ptr1.next, ptr2.next
            pos += 1
            
        return ptr1
        
        
    
