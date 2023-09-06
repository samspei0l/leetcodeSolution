'''
Reverse a Linked List: We know linked list has head which points to first element in list
and a None which points to the end of the list or the next element after the last element in list.
To reverse a list we define our previous to None and our current element to our head.
We store our current.next in temp and our prev in current.next and current in prev and temp in current
Finally we return our previous.
'''


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
