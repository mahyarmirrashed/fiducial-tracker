"""Defines the message protocol model for streaming video data."""

import datetime
import uuid
from dataclasses import dataclass

from .__dict_mixin import DictMixin
from .point import Point


@dataclass(frozen=True)
class VideoStreamRequestMessage(DictMixin):
  """Implements the VideoStream request message arguments."""

  camera_id: uuid.UUID
  frame_encoded: bytes
  timestamp: datetime.datetime
  top_left_corner: Point
  bottom_right_corner: Point

  def get_view_height(self) -> float:
    return abs(self.bottom_right_corner.y - self.top_left_corner.y)

  def get_view_width(self) -> float:
    return abs(self.bottom_right_corner.x - self.top_left_corner.x)


@dataclass(frozen=True)
class VideoStreamResponseMessage(DictMixin):
  """Implements the VideoStream response message arguments."""

  recommended_fps: float
