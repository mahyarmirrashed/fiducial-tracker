"""Defines the message protocol model for streaming location data."""

from dataclasses import dataclass
from typing import List

from .fiducial import Fiducial


@dataclass(frozen=True)
class LocationStreamMessage:
  """Implements the LocationStream message arguments."""

  fiducials: List[Fiducial]
