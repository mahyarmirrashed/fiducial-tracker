from collections import namedtuple
from typing import Tuple

import cv2 as cv
import numpy as np
import zxingcpp
from cachetools import TTLCache

from src.common.models import Fiducial, Point, VideoStreamRequestMessage

_Point = namedtuple("Point", "x y")


def _parse_corners(
  position: zxingcpp.Position,
) -> Tuple[_Point, _Point, _Point, _Point]:
  return (
    _Point(x=position.top_left.x, y=position.top_left.y),
    _Point(x=position.top_right.x, y=position.top_right.y),
    _Point(x=position.bottom_right.x, y=position.bottom_right.y),
    _Point(x=position.bottom_left.x, y=position.bottom_left.y),
  )


def track_fiducial(
  frame: np.ndarray,
  req: VideoStreamRequestMessage,
  cache: TTLCache,
  draw: bool = False,
) -> None:
  height, width, *_ = frame.shape

  for detection in zxingcpp.read_barcodes(frame, formats=zxingcpp.BarcodeFormat.QRCode):
    id = detection.text
    corners = _parse_corners(detection.position)
    top_left, _, bottom_right, _ = corners

    cache[id] = Fiducial(
      id=id,
      location=Point(
        x=(top_left.x + bottom_right.x) // 2,
        y=(top_left.y + bottom_right.y) // 2,
      )
      .normalize(width, height)
      .scale(*req.get_view())
      .add(req.top_left_corner),
      heading=detection.orientation,
    )

    if draw:
      cv.polylines(frame, [np.array(corners, dtype=np.int32)], True, 255)
