"""Defines the message protocol model for streaming location data."""

from dataclasses import dataclass
from typing import List

from .__dict_mixin import DictMixin
from ._fiducial import Fiducial


@dataclass(frozen=True)
class LocationStreamMessage(DictMixin):
  """Implements the LocationStream message arguments."""

  fiducials: List[Fiducial]
