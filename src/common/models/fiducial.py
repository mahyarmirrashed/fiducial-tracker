"""Defines a fiducial model."""

from pydantic import BaseModel, Field, NonNegativeInt
from typing import Optional

import uuid

from ._point import Point


class Fiducial(BaseModel):
  id: uuid.UUID = Field(..., allow_mutation=False)
  location: Point
  heading: Optional[NonNegativeInt]

  class Config:
    validate_assignment = True
