

def check_permutations(string1, string2):
    dict1, dict2 = {}, {}
    for i in string1:
        if not dict1.get(i, None):
            dict1[i] = string1.count(i)
    for i in string2:
        if not dict2.get(i, None):
            dict2[i] = string2.count(i)
    return dict1 == dict2

    # better solution
    # from collections import Counter
    # return Counter(string1) == Counter(string2)

    # better solution 2
    # s1 = s1.lower()
    # s2 = s2.lower()
    # # sort, convert to str and strip
    # s1 = ''.join(sorted(s1)).strip()
    # s2 = ''.join(sorted(s2)).strip()
    # return s1 == s2
