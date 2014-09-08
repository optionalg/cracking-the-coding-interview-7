from prob5 import string_compression


def test_string_compression():
    string1 = 'aabbbccc'
    assert string_compression(string1) == 'a2b3c3'
    string2 = 'abc'
    assert string_compression(string2) == 'abc'