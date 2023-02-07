"""Defines the message protocol model for streaming location data."""

from typing import List

from ._base import BaseMessage
from .fiducial import Fiducial


class LocationStreamMessage(BaseMessage):
  """Implements the LocationStream message arguments."""

  fiducials: List[Fiducial]
