"""Defines a point model."""

from pydantic import NonNegativeInt

from ._frozen_model import FrozenModel


class Point(FrozenModel):
  x: NonNegativeInt
  y: NonNegativeInt
