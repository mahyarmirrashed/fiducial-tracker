"""Defines the message protocol model for streaming video data."""

from typing import Optional

import datetime
import numpy as np
import uuid

from ._base import BaseMessage
from ._point import Point


class VideoStreamRequestMessage(BaseMessage):
  """Implements the VideoStream request message arguments."""

  client_id: uuid.UUID
  frame: np.ndarray
  timestamp: datetime.datetime
  corner_bottom_right: Optional[Point]
  corner_upper_left: Optional[Point]


class VideoStreamResponseMessage(BaseMessage):
  """Implements the VideoStream response message arguments."""

  pass
