from threading import Event, Thread
from typing import List, Union

import cv2 as cv

from src.common import display
from src.common.models import Point

from ._video_reader import VideoReader


class Calibrator:
  def __init__(self, video_reader: VideoReader) -> None:
    self._video_reader = video_reader

    self._calibrated_event = Event()
    self._calibrated_point: Union[Point, None] = None

  def _calibrate_cleanup(self) -> None:
    cv.destroyAllWindows()

  def _calibrate_for(self, corner: str) -> Point:
    self._calibrated_event.clear()
    self._calibrated_point = None
    self._calibrator_title = (
      f"{self._video_reader.camera}: Calibrating for the {corner.lower()} corner..."
    )

    self._calibrator_thread = Thread(target=self._get_calibrated_point, args=(corner,))
    self._calibrator_thread.daemon = True
    self._calibrator_thread.start()

    for frame in self._video_reader.frames():
      cv.imshow(self._calibrator_title, frame)
      cv.waitKey(1)

      if self._calibrated_event.is_set():
        break

    self._calibrate_cleanup()

    assert self._calibrated_point is not None
    return self._calibrated_point

  def _get_calibrated_point(self, corner: str) -> None:
    display(self._calibrator_title)

    while not self._calibrated_event.is_set():
      try:
        user_input = input(f"{corner.capitalize()} coordinate (x,y) >")
        x, y = map(float, user_input.split(","))
      except ValueError:
        display(self._calibrator_title)
        print('Error parsing coordinates in "x,y" form. Please try again.')
        print()
      else:
        self._calibrated_point = Point(x=x, y=y)
        self._calibrated_event.set()

  def calibrate(self) -> List[Point]:
    return [self._calibrate_for("top left"), self._calibrate_for("bottom right")]
