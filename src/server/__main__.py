#!/home/mmirrashed/.conda/envs/tracker/bin/python
import time
from typing import Union

import cv2 as cv
import numpy as np
import qoi
from cachetools import TTLCache
from pyzbar import pyzbar
from pyzbar.locations import Rect
from pyzbar.pyzbar import Decoded

from src.common import Heartbeat
from src.common.models import Fiducial, Point, VideoStreamRequestMessage

from ._args import args
from ._comms import Communicator
from ._diagnostics import show_status
from ._utils import draw_rectangle

camera_cache = TTLCache(maxsize=100, ttl=30)
fiducial_cache = TTLCache(maxsize=10, ttl=5)
fiducial_publisher_heartbeat = Heartbeat(1 / args.frequency)

obj: Decoded
req: Union[VideoStreamRequestMessage, None]


try:
  show_status(args, running=True)

  with Communicator(args.location_stream_address, args.video_stream_address) as comms:
    while req := comms.recv_video_stream():
      # log connected camera uuid
      camera_cache[req.camera_id] = None

      if fiducial_publisher_heartbeat.has_interval_passed():
        comms.send_location_stream(fiducials=list(fiducial_cache.values()))

      processing_start_time = time.time()

      frame: np.ndarray = qoi.decode(req.frame_encoded)
      height, width, _ = frame.shape

      if args.display_raw_frames:
        cv.imshow("Camera stream (raw)", frame)
        cv.waitKey(1)

      for obj in pyzbar.decode(frame):
        bbox: Rect = obj.rect
        identifier = obj.data.decode("utf-8")

        fiducial_cache[identifier] = Fiducial(
          id=identifier,
          location=Point(x=bbox.left + bbox.width // 2, y=bbox.top + bbox.height // 2)
          .normalize(width, height)
          .scale(*req.get_view())
          .add(req.top_left_corner),
        )

        if args.display_processed_frames:
          draw_rectangle(
            frame=frame,
            topleft=(bbox.left, bbox.top),
            bottomright=(bbox.left + bbox.width, bbox.top + bbox.height),
          )

      if args.display_processed_frames:
        cv.imshow("Camera stream (processed)", frame)
        cv.waitKey(1)

      recommended_fps = 1 / (time.time() - processing_start_time)
      recommended_fps_balanced = recommended_fps / len(camera_cache)

      comms.send_video_stream(recommended_fps_balanced)
except KeyboardInterrupt:
  pass
finally:
  show_status(args, running=False)

  cv.destroyAllWindows()
