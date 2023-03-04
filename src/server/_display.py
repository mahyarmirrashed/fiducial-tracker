from typing import Iterable, Set

import cv2 as cv
import numpy as np

_open_windows: Set[str] = set()


def close_old_connection_windows(camera_ids: Iterable[str]) -> None:
  _active_windows = {
    window
    for window in _open_windows
    if any(camera_id in window for camera_id in camera_ids)
  }
  _inactive_windows = _open_windows - _active_windows

  for window in _inactive_windows:
    cv.destroyWindow(window)


def display_frame_in_window(title: str, frame: np.ndarray) -> None:
  _open_windows.add(title)

  cv.imshow(title, frame)
  cv.waitKey(1)
