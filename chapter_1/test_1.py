from prob1 import all_unique, all_unique_without_data


def test_all_unique():
    string1 = 'qwerty'
    assert all_unique(string1) is True
    string2 = 'aabb'
    assert all_unique(string2) is False
    string3 = 'abcdabcd'
    assert all_unique(string3) is False


def test_all_unique_no_data_structures():
    string1 = 'qwerty'
    assert all_unique_without_data(string1) is True
    string2 = 'aabb'
    assert all_unique_without_data(string2) is False