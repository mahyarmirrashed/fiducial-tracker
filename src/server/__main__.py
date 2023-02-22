#!/home/mmirrashed/.conda/envs/tracker/bin/python
import socket
import time
from typing import Union

import cv2 as cv
import numpy as np
import qoi
from cachetools import TTLCache
from pyzbar import pyzbar
from pyzbar.locations import Rect
from pyzbar.pyzbar import Decoded

from src.common import Heartbeat, display
from src.common.models import Fiducial, Point, VideoStreamRequestMessage

from ._args import args
from ._comms import Communicator
from ._utils import draw_rectangle

camera_cache = TTLCache(maxsize=100, ttl=30)
fiducial_cache = TTLCache(maxsize=10, ttl=5)
fiducial_publisher_heartbeat = Heartbeat(1 / args.frequency)

obj: Decoded
req: Union[VideoStreamRequestMessage, None]


def display_diagnostics(*, running: bool) -> None:
  lan_ip_address = socket.gethostbyname(socket.getfqdn())
  server_state = f"\033[1mServer is [{'RUNNING' if running else 'STOPPED'}]:\033[0;0m"

  display(
    f"""{server_state}
  Video stream address:     {lan_ip_address}:{args.video_stream_port}
  Location stream address:  {lan_ip_address}:{args.location_stream_port}
  Publish frequency:        {args.frequency:.2} Hz
  
  Display raw frames:       {"Yes" if args.display_raw_frames else "No"}
  Display processed frames: {"Yes" if args.display_processed_frames else "No"}
  Save raw frames:          {"Yes" if args.save_raw_frames else "No"}
  Save processed frames:    {"Yes" if args.save_processed_frames else "No"}"""
  )


try:
  display_diagnostics(running=True)

  with Communicator(args.location_stream_port, args.video_stream_port) as comms:
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
  display_diagnostics(running=False)

  cv.destroyAllWindows()
