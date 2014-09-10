def merge_sort(uList):
    if len(uList) <= 1:
        return uList
    middle = len(uList) / 2
    right, left = [], []
    for n in uList[:middle]:
        left.append(n)
    for n in uList[middle:]:
        right.append(n)
    print left
    print right
    left = merge_sort(left)
    right = merge_sort(right)
    return _merge(left, right, uList)


def _merge(left, right, uList):
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            uList[k] = left[i]
            k += 1
            i += 1
        else:
            uList[k] = right[j]
            k += 1
            j += 1
    # tidy up, move left overs to uList
    while i < len(left):
        uList[k] = left[i]
        k += 1
        i += 1
    while j < len(right):
        uList[k] = right[j]
        k += 1
        j += 1
    return uList

# followed this vod: https://www.youtube.com/watch?v=TzeBrDU-JaY