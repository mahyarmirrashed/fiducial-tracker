from argparse import ArgumentTypeError
from typing import Any, Tuple


class PointType:
  def __init__(self) -> None:
    pass

  def __call__(self, arg: Any) -> Tuple[float, float]:
    try:
      x, y = map(float, arg.split(","))
    except:
      raise ArgumentTypeError('Coordinates must be in the "x,y" form')
    else:
      return x, y
