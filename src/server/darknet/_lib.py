from ctypes import _NamedFuncPointer, CDLL, c_char_p, c_float, c_int, c_void_p, POINTER
from typing import Any, Union

import os

DEFAULT_NAME_POSIX = "libdarknet.so"
DEFAULT_NAME_WINDOWS = "darknet.dll"


class Library:
  def __init__(self) -> None:
    if os.name == "posix":
      self._load(f"{os.path.dirname(__file__)}/{DEFAULT_NAME_POSIX}")
    elif os.name == "nt":
      os.environ["PATH"] = f"{os.path.dirname(__file__)};{os.environ['PATH']}"
      self._load(DEFAULT_NAME_WINDOWS)
    else:
      raise RuntimeError("Unsupported operating system")

  def _load(self, path: str) -> None:
    self._lib = CDLL(path)
