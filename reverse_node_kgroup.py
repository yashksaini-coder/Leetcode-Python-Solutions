# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        def reverse_list(head, k):
            prev = None
            current = head
            while k > 0:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
                k -= 1
            return prev
        
        def count_nodes(node):
            count = 0
            while node:
                count += 1
                node = node.next
            return count
        
        # Calculate the length of the linked list
        length = count_nodes(head)
        
        # Initialize a dummy node before the head
        dummy = ListNode(0)
        dummy.next = head
        prev_group_end = dummy
        while length >= k:
            group_start = prev_group_end.next
            group_end = group_start
            for _ in range(k - 1):
                group_end = group_end.next
            
            next_group_start = group_end.next
            group_end.next = None
            
            # Reverse the current group and connect it back
            prev_group_end.next = reverse_list(group_start, k)
            group_start.next = next_group_start
            
            prev_group_end = group_start
            length -= k
        
        return dummy.next

sol = Solution()
#test case 1
l=[1,2,3,4,5]
k = 2
print("CASE-1\nList:-",l,"\nk:-",k)
#test case 2
out = sol.reverseKGroup(l,k)