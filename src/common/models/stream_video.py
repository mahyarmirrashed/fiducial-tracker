"""Defines the message protocol model for streaming video data."""

from typing import Optional

import datetime
import uuid

from ._base import BaseMessage
from .point import Point


class VideoStreamRequestMessage(BaseMessage):
  """Implements the VideoStream request message arguments."""

  camera_id: uuid.UUID
  encoded_frame: bytes
  timestamp: datetime.datetime
  bottom_left_corner: Optional[Point]
  top_right_corner: Optional[Point]


class VideoStreamResponseMessage(BaseMessage):
  """Implements the VideoStream response message arguments."""

  pass
