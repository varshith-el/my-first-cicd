import pytest

from calculator import add, subtract


def test_add():
    assert add(1, 2) == 3
    assert add(10, 5) == 15


def test_subtract():
    assert subtract(5, 2) == 3
    assert subtract(10, 3) == 7


@pytest.mark.parametrize("func", [add, subtract])
@pytest.mark.parametrize(
    "a, b",
    [
        ("1", "2"),
        (1, "2"),
        (None, 1),
        (1, None),
        (True, 1),
        ([1], [2]),
    ],
)
def test_rejects_non_numeric_arguments(func, a, b):
    with pytest.raises(TypeError):
        func(a, b)
