"""Defines the message protocol for streaming video data."""

from datetime import datetime
from numpy import ndarray
from typing import Optional
from uuid import UUID

from . import BaseMessage
from ._point import Point


class VideoStreamRequestMessage(BaseMessage):
  """Implements the VideoStream request message arguments."""

  client_id: UUID
  frame: ndarray
  timestamp: datetime
  corner_bottom_right: Optional[Point]
  corner_upper_left: Optional[Point]


class VideoStreamResponseMessage(BaseMessage):
  """Implements the VideoStream response message arguments."""

  pass
