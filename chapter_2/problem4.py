from linked_list import LinkedList


def create_partition(linkedlist, x):
    # if there are nodes in the linked list
    if linkedlist.head is not None:
        # create two pointers
        p1 = linkedlist.head
        p2 = linkedlist.head.next
        while p2 is not None:
            # if the pointer 2 value is less than partition value
            if p2.value < x:
                # remove it from it's place
                p1.next = p2.next
                # move the head to p2.next
                p2.next = linkedlist.head
                # put the current pointer 2 at the head
                linkedlist.head = p2
                # set pointer 2 to pointer 1's next, dont touch pointer 1
                p2 = p1.next
            else:
                p1 = p1.next
                p2 = p1.next