from pydantic import NonNegativeInt
from threading import Event, Thread
from typing import List

from src.common import display
from src.common.models import Point

from ._video_reader import VideoReader

import cv2 as cv


class Calibrator:
  def __init__(self, video_reader: VideoReader) -> None:
    self._video_reader = video_reader

    self._calibrated_event = Event()
    self._calibrated_point: Point

  def _calibrate_for(self, corner: str) -> Point:
    self._calibrated_event.clear()

    Thread(target=self._get_calibrated_point, args=(corner,)).start()

    for frame in self._video_reader.frames():
      cv.imshow(f"Calibrating for the {corner.lower()} corner...", frame)
      cv.waitKey(1)

      if self._calibrated_event.is_set():
        cv.destroyAllWindows()
        break

    return self._calibrated_point

  def _get_calibrated_point(self, corner: str) -> None:
    title = f"Calibrating for the {corner.lower()} corner...\n"

    display(title)

    while user_input := input(f"{corner.capitalize()} coordinate (x,y) >"):
      try:
        x, y = map(float, user_input.split(","))
      except:
        display(title)
        print('Error parsing coordinates in "x,y" form. Please try again.')
        print()
      else:
        self._calibrated_point = Point(x=NonNegativeInt(x), y=NonNegativeInt(y))
        break

    self._calibrated_event.set()

  def calibrate(self) -> List[Point]:
    return [self._calibrate_for("bottom left"), self._calibrate_for("top right")]
