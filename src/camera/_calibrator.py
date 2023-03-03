from threading import Event, Thread
from typing import List, Union

import cv2 as cv

from src.common.models import Point

from ._logger import logger
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
    self._calibrator_title = f"Calibrating {corner.lower()} corner."

    self._calibrator_thread = Thread(target=self._get_calibrated_point, args=(corner,))
    self._calibrator_thread.daemon = True
    self._calibrator_thread.start()

    for frame in self._video_reader.frames():
      cv.imshow(self._calibrator_title, frame)
      cv.waitKey(1)

      if self._calibrated_event.is_set():
        logger.debug(f"{corner.capitalize()} corner calibration completed.")
        break

    self._calibrate_cleanup()

    assert self._calibrated_point is not None
    return self._calibrated_point

  def _get_calibrated_point(self, corner: str) -> None:
    logger.info(self._calibrator_title)

    while not self._calibrated_event.is_set():
      try:
        user_input = input(f"{corner.capitalize()} coordinate (x,y) >")
        x, y = map(float, user_input.split(","))
      except ValueError:
        logger.warn("Unable to parse coordinates. Please retry.")
      else:
        self._calibrated_point = Point(x=x, y=y)
        self._calibrated_event.set()

  def calibrate(self) -> List[Point]:
    logger.info("Starting corner calibration process.")
    corners = [self._calibrate_for("top left"), self._calibrate_for("bottom right")]
    logger.info("Completed corner calibration process.")

    return corners
