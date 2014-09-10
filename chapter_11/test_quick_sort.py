from quick_sort import quick_sort
import random


def test_quick_sort():
    uList = [random.randint(1, 100) for x in range(10000)]
    uList = quick_sort(uList, 0, len(uList)-1)
    assert uList == sorted(uList)