# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = list1
        cur2 = list2

        dummy = ListNode()

        merged = dummy

        while cur1 or cur2:
            if cur1 == None:
                merged.next = cur2
                break

            if cur2 == None:
                merged.next = cur1
                break

            if cur1.val < cur2.val:
                merged.next = cur1
                merged = merged.next
                cur1 = cur1.next
            else:
                merged.next = cur2
                merged = merged.next
                cur2 = cur2.next

        return dummy.next