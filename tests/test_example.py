"""Test the example's public behavior, including its documented input contract."""

import math

import pytest

from pyrverse_port import center


def test_center_accepts_one_pass_iterables_without_mutating_input() -> None:
    values = [1.0, 2.0, 6.0]
    assert center(iter(values)) == (-2.0, -1.0, 3.0)
    assert values == [1.0, 2.0, 6.0]


def test_constant_sequence_is_zero() -> None:
    assert center([7.0, 7.0, 7.0]) == (0.0, 0.0, 0.0)


def test_singleton_is_zero() -> None:
    assert center([4.0]) == (0.0,)


def test_translation_invariance() -> None:
    values = [-3.25, 0.5, 2.75, 10.0]
    assert center([value + 100 for value in values]) == pytest.approx(
        center(values), abs=1e-12, rel=1e-12
    )


def test_empty_sequence_is_rejected() -> None:
    with pytest.raises(ValueError, match="at least one"):
        center([])


@pytest.mark.parametrize("value", [math.nan, math.inf, -math.inf])
def test_nonfinite_values_are_rejected(value: float) -> None:
    with pytest.raises(ValueError, match="finite"):
        center([1.0, value])


def test_unrepresentable_result_is_rejected() -> None:
    with pytest.raises(OverflowError):
        center([-1.6e308, 1.6e308, 1.6e308])
