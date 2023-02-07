from pydantic import NonNegativeInt
from types import TracebackType
from typing import Generator, Union
from typing_extensions import Self

import cv2 as cv
import numpy as np


class VideoReader:
  def __init__(self, source: Union[NonNegativeInt, str]) -> None:
    """Wrapper for OpenCV video reading interactions."""
    self._cap = cv.VideoCapture(source)

    if self._cap is None or not self._cap.isOpened():
      raise ValueError(f"Unable to open video source: {source}")

  def __enter__(self) -> Self:
    return self

  def __exit__(
    self,
    exc_type: Union[BaseException, None],
    exc_value: Union[BaseException, None],
    traceback: Union[TracebackType, None],
  ) -> None:
    self._cap.release()

  def frames(self) -> Generator[np.ndarray, None, None]:
    retval, image = self._cap.read()
    while retval:
      yield image
      retval, image = self._cap.read()
