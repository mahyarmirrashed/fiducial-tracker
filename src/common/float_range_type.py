from argparse import ArgumentTypeError
from typing import Any, Union


class FloatRangeType:
  def __init__(
    self, lower: Union[int, float, None] = None, upper: Union[int, float, None] = None
  ) -> None:
    """Validates that a provided float is within range. Behaves similar to range()."""
    if not FloatRangeType._is_number_or_none(lower):
      raise TypeError("Lower bound must be None or a float")
    if not FloatRangeType._is_number_or_none(upper):
      raise TypeError("Upper bound must be None or a float")

    self._lower = lower
    self._upper = upper

  def __call__(self, arg: Any) -> float:
    try:
      value = float(arg)
    except ValueError:
      raise ArgumentTypeError("Must be a float")

    if not self._within_range(value):
      raise self._range_exception()

    return value

  @staticmethod
  def _is_number_or_none(value: Union[int, float, None]) -> bool:
    return value is None or isinstance(value, (int, float))

  def _range_exception(self) -> ArgumentTypeError:
    if self._lower is None:
      return ArgumentTypeError(f"Must be a number < {self._upper}")
    elif self._upper is None:
      return ArgumentTypeError(f"Must be a number >= {self._lower}")
    else:
      return ArgumentTypeError(f"Must be a number in [{self._lower}, {self._upper})")

  def _within_lower_range(self, value: Union[int, float]) -> bool:
    return self._lower is None or value >= self._lower

  def _within_upper_range(self, value: Union[int, float]) -> bool:
    return self._upper is None or value < self._upper

  def _within_range(self, value: Union[int, float]) -> bool:
    return self._within_lower_range(value) and self._within_upper_range(value)
