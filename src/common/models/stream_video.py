"""Defines the message protocol model for streaming video data."""

from typing import Optional

import datetime
import uuid

from ._base import BaseMessage
from ._point import Point

from src.common.models.custom import NDArrayUint8


class VideoStreamRequestMessage(BaseMessage):
  """Implements the VideoStream request message arguments."""

  client_id: uuid.UUID
  frame: NDArrayUint8
  timestamp: datetime.datetime
  corner_bottom_right: Optional[Point]
  corner_upper_left: Optional[Point]


class VideoStreamResponseMessage(BaseMessage):
  """Implements the VideoStream response message arguments."""

  pass
