from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"
    assert arrs.get([-1, 1, 2], 0) == -1
    assert arrs.get([], 0) == None
    assert arrs.get([], -1) == None



def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == []
    assert arrs.my_slice([1, 2, 3], 1) == []
    assert arrs.my_slice([]) == []
    assert arrs.my_slice([1, 2, 3, 4], -5, 2) == [1, 2]
    assert arrs.my_slice([1, 2, 3, 4], -3, 3) == [1, 2, 3]
    assert arrs.my_slice([1, 2, 3, 4], -4, 3) == [1, 2, 3]
    assert arrs.my_slice([1, 2, 3, 4], 1, -2) == []
    assert arrs.my_slice([1, 2, 3, 4], 0, 0) == []
    assert arrs.my_slice([0], -5, 3) == [0]
    assert arrs.my_slice([1, 2, -3, 4], -5, 3) == [1, 2, -3]
    assert arrs.my_slice([1, 2, 3, 4], 9, 3) == []






