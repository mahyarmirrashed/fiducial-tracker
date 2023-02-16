from ctypes import c_void_p
from dataclasses import dataclass, field
from random import randrange
from typing import Dict, List, Tuple


@dataclass(frozen=True)
class BoundingBox:
  x: float
  y: float
  w: float
  h: float

  def corners(self) -> Tuple[int, int, int, int]:
    xmin = int(round(self.x - (self.w / 2)))
    xmax = int(round(self.x + (self.w / 2)))
    ymin = int(round(self.y - (self.h / 2)))
    ymax = int(round(self.y + (self.h / 2)))

    return xmin, ymin, xmax, ymax


@dataclass(frozen=True)
class Color:
  r: int = field(default_factory=lambda: randrange(0, 256), init=False)
  g: int = field(default_factory=lambda: randrange(0, 256), init=False)
  b: int = field(default_factory=lambda: randrange(0, 256), init=False)

  def bgr(self) -> Tuple[int, int, int]:
    return (self.b, self.g, self.r)

  def rgb(self) -> Tuple[int, int, int]:
    return (self.r, self.g, self.b)


@dataclass(frozen=True)
class Network:
  network: c_void_p
  width: int
  height: int
  class_names: List[str]
  class_colors: Dict[str, Color] = field(init=False)

  def __post_init__(self) -> None:
    object.__setattr__(self, "class_colors", self._generate_colors(self.class_names))

  @staticmethod
  def _generate_colors(names: List[str]) -> Dict[str, Color]:
    return {name: Color() for name in names}


@dataclass
class Prediction:
  class_name: str
  confidence: float
  bounding_box: BoundingBox
