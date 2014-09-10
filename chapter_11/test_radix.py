from radix_sort import radix_sort
import random


def test_radix_sort():
    uList = [random.randint(1, 10000000) for x in range(10000)]
    sList = radix_sort(uList)
    assert sList == sorted(uList)

