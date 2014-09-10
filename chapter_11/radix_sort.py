

def radix_sort(uList):
    sorting = True
    m = 10
    n = 1
    calls = 0
    while sorting:
        buckets = [[] for x in range(10)]
        for i in uList:
            b = i
            b = b % m
            b = b / n
            buckets[b].append(i)
        if len(buckets[0]) == len(uList):
            sorting = False
        else:
            uList = []
            for i in range(10):
                for x in buckets[i]:
                    uList.append(x)
            m *= 10
            n *= 10
            calls +=1
    return uList
