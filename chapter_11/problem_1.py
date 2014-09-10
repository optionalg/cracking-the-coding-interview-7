
def problem1_merge(a, b):
    c = a[:]
    i = j = k = 0
    while i < len(a) and j < len(b):
        if b[j] <= c[k]:
            c[k] = b[j]
            k += 1
            j += 1
        else:
            c[k] = a[i]
            k += 1
            i += 1
    while i < len(a):
        c[k] = a[i]
        k += 1
        i += 1
    while j < len(b):
        c[k] = b[j]
        k += 1
        j += 1
    return c