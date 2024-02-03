from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f'{self.val}'


def create_head() -> ListNode:
    x = ListNode(1)
    y = ListNode(2)
    w = ListNode(3)
    z = ListNode(4)
    l = ListNode(5)
    x.next = y
    y.next = w
    w.next = z
    z.next = l
    return x


def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    dummy = ListNode(0)
    dummy.next = head
    length = 0
    first = head  # указатель на head который мы будем двигать чтобы посчитать длину связного списка
    while first:
        length += 1
        first = first.next
    length -= n
    first = dummy
    while length > 0:
        length -= 1
        first = first.next  # после цикла мы остановимся перед нодой которую нужно удалить
    first.next = first.next.next
    return dummy.next


# def removeNthFromEnd_2(head: Optional[ListNode], n: int) -> Optional[ListNode]:
#     dummy = ListNode(None, head)
#     first, second = dummy, dummy
#     for i in range(n + 1): first = first.next
#     while first: first, second = first.next, second.next
#     # как только first перестанет существовать мы окажемся на 3
#     second.next = second.next.next
#     return dummy.next


head = create_head()

x = removeNthFromEnd(head, 2)

