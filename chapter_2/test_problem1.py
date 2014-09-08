from linked_list import Node, LinkedList
from problem1 import remove_dups


def test_remove_dups():
    list1 = LinkedList()
    list1.addNode('peanut')
    list1.addNode('davey')
    list1.addNode('dog')
    list1.addNode('peanut')
    list1.addNode('hearts')
    list1.addNode('dog')
    remove_dups(list1)
    assert list1.head.next.next.next.value == 'hearts'
