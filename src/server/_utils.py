from typing import Tuple

import cv2 as cv
import numpy as np

_RED = (0, 0, 255)


def draw_rectangle(
  *,
  frame: np.ndarray,
  topleft: Tuple[int, int],
  bottomright: Tuple[int, int],
  color: Tuple[int, int, int] = _RED,
  thickness=1,
):
  cv.rectangle(frame, topleft, bottomright, color, thickness)
