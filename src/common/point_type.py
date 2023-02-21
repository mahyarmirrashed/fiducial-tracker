from argparse import ArgumentTypeError
from typing import Any

from src.common.models import Point


class PointType:
  def __init__(self) -> None:
    pass

  def __call__(self, arg: Any) -> Point:
    try:
      x, y = map(float, arg.split(","))
    except:
      raise ArgumentTypeError('Coordinates must be in the "x,y" form')
    else:
      return Point(x=x, y=y)
