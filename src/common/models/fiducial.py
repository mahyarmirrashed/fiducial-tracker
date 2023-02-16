"""Defines a fiducial model."""

from dataclasses import dataclass
from typing import Optional

from .point import Point


@dataclass
class Fiducial:
  id: str
  location: Point
  heading: Optional[int]
