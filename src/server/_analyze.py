import numpy as np
from cachetools import TTLCache
from pyzbar import pyzbar
from pyzbar.locations import Rect
from pyzbar.pyzbar import Decoded

from src.common.models import Fiducial, Point, VideoStreamRequestMessage

from ._utils import draw_rectangle

obj: Decoded
bbox: Rect


def track_fiducial(
  frame: np.ndarray,
  req: VideoStreamRequestMessage,
  cache: TTLCache,
  draw: bool = False,
) -> None:
  width, height, *_ = frame.shape

  for obj in pyzbar.decode(frame, symbols=[pyzbar.ZBarSymbol.QRCODE]):
    bbox: Rect = obj.rect
    identifier = obj.data.decode("utf-8")

    cache[identifier] = Fiducial(
      id=identifier,
      location=Point(x=bbox.left + bbox.width // 2, y=bbox.top + bbox.height // 2)
      .normalize(width, height)
      .scale(*req.get_view())
      .add(req.top_left_corner),
    )

    if draw:
      draw_rectangle(
        frame=frame,
        topleft=(bbox.left, bbox.top),
        bottomright=(bbox.left + bbox.width, bbox.top + bbox.height),
      )
