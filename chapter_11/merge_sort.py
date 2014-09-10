def merge_sort(uList):
    if uList <= 1:
        return uList
    middle = len(uList) / 2
    right, left = [], []
    for n in uList[:middle]:
        right.append(n)
    for n in uList[middle:]:
        left.append(n)
    right = merge_sort(right)
    left = merge_sort(left)
    return _merge(right, left)


def _merge(right, left, uList):
    i = j = k = 0
    while i < len(right) and j < len(left):
        if right[i] <= left[j]:
            uList[k] = right[i]
            k += 1
            i += 1
        else:
            uList[k] = left[j]
            k += 1
            j += 1
    while i < len(right):
        uList[k] = right[i]
        k += 1
        i += 1
    while j < len(left):
        uList[k] = left[k]
        k += 1
        j += 1
    return uList
