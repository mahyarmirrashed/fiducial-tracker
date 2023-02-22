"""Defines a fiducial model."""

from dataclasses import dataclass

from ._point import Point


@dataclass
class Fiducial:
  id: str
  location: Point
