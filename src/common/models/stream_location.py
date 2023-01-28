"""Defines the message protocol model for streaming location data."""

from pydantic import NonNegativeInt
from typing import Optional

import uuid

from ._base import BaseMessage
from ._point import Point


class LocationStreamRPCRequest(BaseMessage):
  """Implements the LocationStream request message arguments."""

  fiducial_id: uuid.UUID
  location: Point
  heading: Optional[NonNegativeInt]


class LocationStreamRPCResponse(BaseMessage):
  """Implements the LocationStream response message arguments."""

  pass
