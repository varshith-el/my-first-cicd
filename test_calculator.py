import pytest

from calculator import add, subtract


def test_add():
    assert add(1, 2) == 3
    assert add(10, 5) == 15


def test_subtract():
    assert subtract(5, 2) == 3
    assert subtract(10, 3) == 7


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (0, 0, 0),
        (0, 7, 7),
        (-1, -2, -3),
        (-5, 3, -2),
        (2**62, 2**62, 2**63),
    ],
)
def test_add_integers(a, b, expected):
    assert add(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (0, 0, 0),
        (0, 7, -7),
        (-1, -2, 1),
        (-5, 3, -8),
        (2**63, 2**62, 2**62),
    ],
)
def test_subtract_integers(a, b, expected):
    assert subtract(a, b) == expected


def test_add_floats():
    assert add(0.1, 0.2) == pytest.approx(0.3)
    assert add(1.5, -2.5) == pytest.approx(-1.0)


def test_subtract_floats():
    assert subtract(0.3, 0.1) == pytest.approx(0.2)
    assert subtract(-1.5, 2.5) == pytest.approx(-4.0)


def test_add_is_commutative():
    assert add(3, 9) == add(9, 3)


def test_subtract_is_inverse_of_add():
    assert subtract(add(8, 4), 4) == 8


def test_add_concatenates_sequences():
    assert add("ab", "cd") == "abcd"
    assert add([1], [2]) == [1, 2]


@pytest.mark.parametrize("func", [add, subtract])
def test_unsupported_operand_types_raise(func):
    with pytest.raises(TypeError):
        func("1", 2)


def test_subtract_rejects_strings():
    with pytest.raises(TypeError):
        subtract("ab", "a")
