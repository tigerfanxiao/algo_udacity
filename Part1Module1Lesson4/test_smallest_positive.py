from Part1Module1Lesson4.smallest_postive import smallest_positive


def test_smallest_positive():
    assert smallest_positive([4, -6, 7, 2, -4, 10]) == 2
    assert smallest_positive([.2, 5, 3, -.1, 7, 7, 6]) == 0.2
    assert smallest_positive([-6, -9, -7]) is None
    assert smallest_positive([]) is None



