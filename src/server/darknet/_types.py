from ctypes import c_void_p
from random import randrange
from typing import Dict, List, Tuple

from ._structures import MetadataStruct


class Color:
  def __init__(self) -> None:
    self._r = randrange(0, 256)
    self._g = randrange(0, 256)
    self._b = randrange(0, 256)

  def bgr(self) -> Tuple[int, int, int]:
    return (self._b, self._g, self._r)

  def rgb(self) -> Tuple[int, int, int]:
    return (self._r, self._g, self._b)


class Network:
  def __init__(self, *, network: c_void_p, metadata: MetadataStruct) -> None:
    self._network = network
    self._class_names = list(map(lambda name: name.decode("ascii"), metadata.names))
    self._class_colors = self._generate_class_colors(self._class_names)

  @staticmethod
  def _generate_class_colors(names: List[str]) -> Dict[str, Color]:
    return {name: Color() for name in names}

  def get(self) -> c_void_p:
    return self._network

  def get_class_colors(self) -> Dict[str, Color]:
    return self._class_colors

  def get_class_names(self) -> List[str]:
    return self._class_names
