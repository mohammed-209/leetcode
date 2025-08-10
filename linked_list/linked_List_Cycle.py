# 141.Linked List Cycle
# https://leetcode.com/problems/linked-list-cycle/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        while head:
            if head in visited:
                return True
            visited.add(head)
            head = head.next
        return False


        # slow, fast = head, head


        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next
        #     if slow == fast:
        #         return True
        # return False

#recursive
#------------------------------------------------------------------------
        
        # s = set()

        # def _hasCycle(head):
        #     if not head:
        #         return False

        #     if head in s:
        #         return True 
        #     s.add(head)
        #     return _hasCycle(head.next)
        
        # return _hasCycle(head)