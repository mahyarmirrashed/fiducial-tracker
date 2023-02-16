"""Defines a fiducial model."""

from dataclasses import dataclass
from typing import Optional

import uuid

from .point import Point


@dataclass
class Fiducial:
  id: uuid.UUID
  location: Point
  heading: Optional[int]
