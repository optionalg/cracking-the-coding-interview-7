from problem4 import create_partition
from linked_list import LinkedList


def test_create_partition():
    list1 = LinkedList()
    list1.addNode(3)
    list1.addNode(1)
    list1.addNode(2)
    create_partition(list1, 2)
    assert list1.head.value == 1
    assert list1.head.next.value == 2
    assert list1.head.next.next.value == 3