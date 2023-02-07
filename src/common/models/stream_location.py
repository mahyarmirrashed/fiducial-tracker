"""Defines the message protocol model for streaming location data."""

from typing import List

from ._base import BaseMessage
from .fiducial import Fiducial


class LocationStreamRequestMessage(BaseMessage):
  """Implements the LocationStream request message arguments."""

  fiducials: List[Fiducial]


class LocationStreamResponseMessage(BaseMessage):
  """Implements the LocationStream response message arguments."""

  pass
