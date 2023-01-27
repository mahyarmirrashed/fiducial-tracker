"""Defines the message protocol for streaming video data."""

from datetime import datetime
from numpy import ndarray
from pydantic import NonNegativeInt
from typing import Tuple
from uuid import UUID

from . import BaseMessage


class VideoStreamRequestMessage(BaseMessage):
  """Implements the VideoStream request message arguments."""

  client_id: UUID
  frame: ndarray
  timestamp: datetime
  corner_bottom_right: Tuple[NonNegativeInt, NonNegativeInt]
  corner_upper_left: Tuple[NonNegativeInt, NonNegativeInt]


class VideoStreamResponseMessage(BaseMessage):
  """Implements the VideoStream response message arguments."""

  pass
