class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solution(l1: ListNode, l2: ListNode) -> ListNode:
    head = ListNode(0)
    tail = head
    carry = 0

    while l1 is not None or l2 is not None or carry != 0:

        digit_1 = l1.val if l1 is not None else 0
        digit_2 = l2.val if l2 is not None else 0

        summ = digit_1 + digit_2 + carry
        digit = summ % 10
        carry = summ // 10

        newNode = ListNode(digit)
        tail.next = newNode
        tail = tail.next

        l1 = l1.next if l1 is not None else None
        l2 = l2.next if l2 is not None else None

    result = head.next
    head.next = None
    return result

