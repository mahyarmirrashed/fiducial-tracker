"""Defines a point model."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Point:
  x: int
  y: int
