
def _partition(uList, start, end):
        # for this quicksort implementation, pivot is the end of list
        pivot = uList[end]
        # create pointer that starts at beginning
        p_index = start
        for i in range(start, end):
            if uList[i] <= pivot:
                uList[i], uList[p_index] = uList[p_index], uList[i]
                p_index += 1
        # make final swap
        uList[p_index], uList[end] = uList[end], uList[p_index]
        return p_index


def quick_sort(uList, start, end):
    if start < end:
        p_index = _partition(uList, start, end)
        quick_sort(uList, start, (p_index-1))
        quick_sort(uList, (p_index+1), end)
    return uList
