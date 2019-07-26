from utils import construct_linklist, ListNode


def print_list_reverse(head: ListNode) -> list:
    stack, h = [], head
    while h:
        stack.append(h.val)
        h = h.next
    return stack[::-1]

l1 = (1, 2, 3, 4, 5)
print(l1)
l1 = construct_linklist(l1)
lst1 = print_list_reverse(l1)
print(lst1)
l2 = [3, 4, 8, 2, 7]
print(l2)
l2 = construct_linklist(l2)
lst2 = print_list_reverse(l2)
print(lst2)
