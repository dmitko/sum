import sum


def test_my_sum():
    assert sum.my_sum(1, 2) == 3

def test_failed():
    assert sum.my_sum(2, 4) == 5
