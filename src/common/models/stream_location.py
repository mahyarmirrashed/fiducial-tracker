"""Defines the message protocol for streaming location data."""

from pydantic import NonNegativeInt
from uuid import UUID

from . import BaseMessage
from ._point import Point


class LocationStreamRPCRequest(BaseMessage):
  """Implements the LocationStream request message arguments."""

  fiducial_id: UUID
  location: Point
  heading: NonNegativeInt


class LocationStreamRPCResponse(BaseMessage):
  """Implements the LocationStream response message arguments."""

  pass
