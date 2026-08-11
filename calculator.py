"""Simple arithmetic helpers with explicit input validation."""

from numbers import Real


def _as_number(name, value):
    """Return value if it is a real number, otherwise raise TypeError."""
    if isinstance(value, bool) or not isinstance(value, Real):
        raise TypeError(
            f"{name} must be a real number, got {type(value).__name__}: {value!r}"
        )
    return value


def add(a, b):
    return _as_number("a", a) + _as_number("b", b)


def subtract(a, b):
    return _as_number("a", a) - _as_number("b", b)
