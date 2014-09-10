

def radix_sort(uList):
    sorting = True
    m = 10
    n = 1
    while sorting:
        buckets = [[] for x in range(10)]
        for i in uList:
            b = i
            b = b % m
            b = b % n
            i.append[buckets[b]]
        if len(buckets[0]) == len(uList):
            sorting = False
        else:
            uList = []
            for i in range(10):
                for n in buckets[i]:
                    uList.append(n)
            m *= 10
            n *= 10
    return uList
