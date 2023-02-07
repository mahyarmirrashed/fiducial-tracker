from pydantic import NonNegativeInt
from types import TracebackType
from typing import Generator, Union
from typing_extensions import Self

import cv2 as cv
import numpy as np
import time

DEFAULT_FPS = 30


class VideoReader:
  def __init__(self, src: Union[NonNegativeInt, str], fps: int = DEFAULT_FPS) -> None:
    """Wrapper for OpenCV video reading interactions."""
    self._cap = cv.VideoCapture(src)
    self._fps = fps

    self._prev_frame_time = 0

    if self._cap is None or not self._cap.isOpened():
      raise ValueError(f"Unable to open video source: {src}")

  def __enter__(self) -> Self:
    return self

  def __exit__(
    self,
    exc_type: Union[BaseException, None],
    exc_value: Union[BaseException, None],
    traceback: Union[TracebackType, None],
  ) -> None:
    self._cap.release()

  def _regulate_fps(self) -> None:
    elapsed_time = time.time() - self._prev_frame_time

    if elapsed_time < 1.0 / self._fps:
      time.sleep(1.0 / self._fps - elapsed_time)

    self._prev_frame_time = time.time()

  @property
  def fps(self) -> NonNegativeInt:
    return self._fps

  @fps.setter
  def fps(self, new_fps: NonNegativeInt) -> None:
    if not isinstance(new_fps, (int, float)):
      raise TypeError("fps must be an integer or float")
    elif new_fps <= 0:
      raise ValueError("fps must be non-negative")
    else:
      self._fps = new_fps

  def frames(self) -> Generator[np.ndarray, None, None]:
    prev = 0
    retval, image = self._cap.read()

    while retval:
      self._regulate_fps()

      yield image

      retval, image = self._cap.read()
