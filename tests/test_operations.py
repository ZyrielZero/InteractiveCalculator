import pytest
from typing import Union
from src.operations import Operations

Number = Union[int, float]


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (8, 5, 13),
        (12, -4, 8),
        (-7, -6, -13),
        (3.5, 1.5, 5.0),
        (-9.25, 4.25, -5.0),
    ],
    ids=[
        "positive_integers",
        "positive_and_negative",
        "two_negatives",
        "positive_floats",
        "negative_and_positive_float",
    ],
)
def test_addition(a: Number, b: Number, expected: Number) -> None:
    result = Operations.addition(a, b)
    assert result == expected, f"Expected addition({a}, {b}) == {expected}, got {result}"


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (15, 9, 6),
        (4, 10, -6),
        (-8, -3, -5),
        (7.75, 2.25, 5.5),
        (-6.5, -2.5, -4.0),
    ],
    ids=[
        "positive_integers",
        "result_goes_negative",
        "two_negatives",
        "positive_floats",
        "two_negative_floats",
    ],
)
def test_subtraction(a: Number, b: Number, expected: Number) -> None:
    result = Operations.subtraction(a, b)
    assert result == expected, f"Expected subtraction({a}, {b}) == {expected}, got {result}"


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (6, 7, 42),
        (9, 0, 0),
        (-4, -5, 20),
        (1.5, 6.0, 9.0),
        (-3.5, 2.0, -7.0),
    ],
    ids=[
        "positive_integers",
        "times_zero",
        "two_negatives",
        "positive_floats",
        "negative_times_positive",
    ],
)
def test_multiplication(a: Number, b: Number, expected: Number) -> None:
    result = Operations.multiplication(a, b)
    assert result == expected, f"Expected multiplication({a}, {b}) == {expected}, got {result}"


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (18, 6, 3.0),
        (-20, -4, 5.0),
        (9.0, 4.0, 2.25),
        (-15.0, 6.0, -2.5),
        (0, 7, 0.0),
    ],
    ids=[
        "positive_integers",
        "two_negatives",
        "positive_floats",
        "negative_by_positive",
        "zero_dividend",
    ],
)
def test_division(a: Number, b: Number, expected: float) -> None:
    result = Operations.division(a, b)
    assert result == expected, f"Expected division({a}, {b}) == {expected}, got {result}"


@pytest.mark.parametrize(
    "a, b",
    [
        (4, 0),
        (-9, 0),
        (2.5, 0),
    ],
    ids=[
        "positive_by_zero",
        "negative_by_zero",
        "float_by_zero",
    ],
)
def test_division_by_zero(a: Number, b: Number) -> None:
    with pytest.raises(ValueError, match="Division by zero is not allowed.") as excinfo:
        Operations.division(a, b)
    assert "Division by zero is not allowed." in str(excinfo.value)