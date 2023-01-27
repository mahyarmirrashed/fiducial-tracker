"""Defines the message protocol for streaming location data."""

from pydantic import NonNegativeInt
from typing import Optional
from uuid import UUID

from . import BaseMessage
from ._point import Point


class LocationStreamRPCRequest(BaseMessage):
  """Implements the LocationStream request message arguments."""

  fiducial_id: UUID
  location: Point
  heading: Optional[NonNegativeInt]


class LocationStreamRPCResponse(BaseMessage):
  """Implements the LocationStream response message arguments."""

  pass
