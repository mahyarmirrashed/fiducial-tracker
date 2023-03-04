from typing import Iterable, Set

import cv2 as cv
import numpy as np


class _DisplayManager:
  def __init__(self) -> None:
    self._open_windows: Set[str] = set()

  def close_old(self, ids: Iterable[str]) -> None:
    _active_windows = {
      window for window in self._open_windows if any(id in window for id in ids)
    }
    _inactive_windows = self._open_windows - _active_windows

    for window in _inactive_windows:
      cv.destroyWindow(window)

    self._open_windows = _active_windows

  def display(self, title: str, frame: np.ndarray) -> None:
    self._open_windows.add(title)

    cv.imshow(title, frame)
    cv.waitKey(1)


display_manager = _DisplayManager()
