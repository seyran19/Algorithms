from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(0)
    first = dummy

    while list1 and list2:
        if list1.val < list2.val:
            first.next = list1
            first, list1 = first.next, list1.next
        else:
            first.next = list2
            first, list2 = first.next, list2.next

    if list1:
        first.next = list1
    elif list2:
        first.next = list2
    return dummy.next
