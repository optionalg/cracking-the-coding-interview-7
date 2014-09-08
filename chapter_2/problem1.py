from linked_list import Node, LinkedList


def remove_dups(linked_list):
    if (linked_list.head):
        current = linked_list.head
        table = {current.value: True}
        while current.next:
            if current.next.value in table:
                print current.next.value
                current.next = current.next.next
            else:
                table[current.next.value] = True
                current = current.next
