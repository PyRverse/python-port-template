"""A small, dependency-free example to exercise the package infrastructure."""

from collections.abc import Iterable
from math import isfinite
from statistics import fmean


def center(values: Iterable[float]) -> tuple[float, ...]:
    """Subtract the arithmetic mean from a nonempty, finite sequence.

    This teaching example has no missing-value handling or scientific parity
    claim. It materializes the iterable and returns new values in input order.

    Raises:
        ValueError: If input is empty or contains a nonfinite value.
        OverflowError: If the intermediate sum or a centered value overflows.
    """
    data = tuple(float(value) for value in values)
    if not data:
        raise ValueError("values must contain at least one number")
    if not all(isfinite(value) for value in data):
        raise ValueError("values must be finite")
    mean = fmean(data)
    result = tuple(value - mean for value in data)
    if not all(isfinite(value) for value in result):
        raise OverflowError("centered values cannot be represented as finite floats")
    return result
