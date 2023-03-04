"""Defines a fiducial model."""

from dataclasses import dataclass

from .__dict_mixin import DictMixin
from ._point import Point


@dataclass
class Fiducial(DictMixin):
  id: str
  location: Point
  heading: int
