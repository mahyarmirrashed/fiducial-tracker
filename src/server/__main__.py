#!/home/mmirrashed/.conda/envs/tracker/bin/python
from cachetools import TTLCache
from pyzbar import pyzbar
from pyzbar.locations import Rect
from pyzbar.pyzbar import Decoded
from typing import Union

from src.common import display
from src.common.models import Fiducial, Point, VideoStreamRequestMessage

from ._args import args
from ._comms import Communicator

import cv2 as cv
import qoi
import socket
import time


DEFAULT_RECOMMENDED_FPS = 300


camera_cache = TTLCache(maxsize=100, ttl=30)
fiducial_cache = TTLCache(maxsize=10, ttl=5)

decoder = lambda obj: obj.data.decode("utf-8")

obj: Decoded
req: Union[VideoStreamRequestMessage, None]


def display_diagnostics(*, running: bool) -> None:
  lan_ip_address = socket.gethostbyname(socket.getfqdn())
  server_state = f"\033[1mServer is [{'RUNNING' if running else 'STOPPED'}]:\033[0;0m"

  display(
    f"""{server_state}
  Video stream address:     {lan_ip_address}:{args.video_stream_port}
  Location stream address:  {lan_ip_address}:{args.location_stream_port}
  
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

      start = time.time()

      frame = qoi.decode(req.frame_encoded)

      for obj in pyzbar.decode(frame):
        bbox: Rect = obj.rect
        identifier = obj.data.decode("utf-8")

        fiducial_cache[identifier] = Fiducial(
          id=identifier,
          location=Point(x=bbox.left + bbox.width // 2, y=bbox.top + bbox.height // 2),
        )

      recommended_fps = 1 / (time.time() - start)
      recommended_fps_balanced = recommended_fps / len(camera_cache)

      comms.send_video_stream(recommended_fps_balanced)
except KeyboardInterrupt:
  pass
finally:
  display_diagnostics(running=False)

  cv.destroyAllWindows()
