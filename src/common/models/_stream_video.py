"""Defines the message protocol model for streaming video data."""

import datetime
import math
import uuid
from dataclasses import dataclass
from typing import Tuple

from .__dict_mixin import DictMixin
from ._point import Point


@dataclass(frozen=True)
class VideoStreamRequestMessage(DictMixin):
  """Implements the VideoStream request message arguments."""

  camera_id: uuid.UUID
  frame: bytes
  shape: Tuple[int, ...]
  timestamp: datetime.datetime
  top_left_corner: Point
  bottom_right_corner: Point

  def _get_view_height(self) -> float:
    return self.bottom_right_corner.y - self.top_left_corner.y

  def _get_view_width(self) -> float:
    return self.bottom_right_corner.x - self.top_left_corner.x

  def get_rotation(self) -> float:
    dx = self.bottom_right_corner.x - self.top_left_corner.x
    dy = self.bottom_right_corner.y - self.top_left_corner.y

    return (math.atan2(dy, dx) * (180 / math.pi)) - 45

  def get_view(self) -> Tuple[float, float]:
    return (self._get_view_width(), self._get_view_height())


@dataclass(frozen=True)
class VideoStreamResponseMessage(DictMixin):
  """Implements the VideoStream response message arguments."""

  recommended_fps: float
