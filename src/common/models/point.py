"""Defines a point model."""

from dataclasses import dataclass

from typing_extensions import Self


@dataclass(frozen=True)
class Point:
  x: float
  y: float

  def __add__(self, other: Self) -> Self:
    return Point(x=self.x + other.x, y=self.y + other.y)

  def __sub__(self, other: Self) -> Self:
    return Point(x=self.x - other.x, y=self.y - other.y)

  def add(self, other: Self) -> Self:
    return self + other

  def normalize(self, x_ref: float, y_ref: float) -> Self:
    return Point(x=self.x / x_ref, y=self.y / y_ref)

  def scale(self, x_scale: float, y_scale: float) -> Self:
    return Point(x=self.x * x_scale, y=self.y * y_scale)
