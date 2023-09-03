class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        fast = slow = dummy
        
        # Move fast pointer n steps ahead
        for _ in range(n + 1):
            fast = fast.next
        
        # Move fast and slow pointers until fast reaches the end
        while fast:
            fast = fast.next
            slow = slow.next
        
        # Remove the nth node from the end
        slow.next = slow.next.next
        
        return dummy.next

# Helper function to create a linked list from a list
def create_linked_list(values):
    dummy = ListNode(0)
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Helper function to convert linked list to list
def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Test cases
solution = Solution()
head1 = create_linked_list([1,2,3,4,5])
result1 = solution.removeNthFromEnd(head1, 2)
print(linked_list_to_list(result1))  # Output: [1, 2, 3, 5]
print_linked_list(head1)


head2 = create_linked_list([1])
result2 = solution.removeNthFromEnd(head2, 1)
print(linked_list_to_list(result2))  # Output: []
print_linked_list(head2)

head3 = create_linked_list([1,2])
result3 = solution.removeNthFromEnd(head3, 1)
print(linked_list_to_list(result3))  # Output: [1]
print_linked_list(head3)

head = create_linked_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print_linked_list(head)