"""Defines the message protocol model for streaming video data."""

import datetime
import uuid
from dataclasses import dataclass

from .point import Point


@dataclass(frozen=True)
class VideoStreamRequestMessage:
  """Implements the VideoStream request message arguments."""

  camera_id: uuid.UUID
  frame_encoded: bytes
  timestamp: datetime.datetime
  bottom_left_corner: Point
  top_right_corner: Point

  def get_view_height(self) -> float:
    return abs(self.top_right_corner.y - self.bottom_left_corner.y)

  def get_view_width(self) -> float:
    return abs(self.top_right_corner.x - self.bottom_left_corner.x)


@dataclass(frozen=True)
class VideoStreamResponseMessage:
  """Implements the VideoStream response message arguments."""

  recommended_fps: float
