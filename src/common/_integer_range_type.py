from argparse import ArgumentTypeError
from typing import Any, Union


class IntegerRangeType:
  def __init__(
    self, lower: Union[int, None] = None, upper: Union[int, None] = None
  ) -> None:
    """Validates that a provided integer is within range. Behaves similar to range()."""
    if not IntegerRangeType._is_int_or_none(lower):
      raise ValueError("Lower bound must be None or an integer")
    if not IntegerRangeType._is_int_or_none(upper):
      raise ValueError("Upper bound must be None or an integer")

    self._lower = lower
    self._upper = upper

  def __call__(self, arg: Any) -> int:
    try:
      value = int(arg)
    except ValueError:
      raise ArgumentTypeError("Must be an integer")

    if not self._within_range(value):
      raise self._range_exception()

    return value

  @staticmethod
  def _is_int_or_none(value: Union[int, None]) -> bool:
    return value is None or isinstance(value, int)

  def _range_exception(self) -> ArgumentTypeError:
    if self._lower is None:
      return ArgumentTypeError(f"Must be an integer < {self._upper}")
    elif self._upper is None:
      return ArgumentTypeError(f"Must be an integer >= {self._lower}")
    else:
      return ArgumentTypeError(f"Must be an integer in [{self._lower}, {self._upper})")

  def _within_lower_range(self, value: int) -> bool:
    return self._lower is None or value >= self._lower

  def _within_upper_range(self, value: int) -> bool:
    return self._upper is None or value < self._upper

  def _within_range(self, value: int) -> bool:
    return self._within_lower_range(value) and self._within_upper_range(value)
