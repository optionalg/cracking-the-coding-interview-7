from prob3 import check_permutations


def test_check_permutations():
    string1 = 'abc'
    string2 = 'cba'
    assert check_permutations(string1, string2) is True
    string1 = 'cassy'
    string2 = 'dassy'
    assert check_permutations(string1, string2) is False