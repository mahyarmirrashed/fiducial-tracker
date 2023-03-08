#!/home/mmirrashed/.conda/envs/tracker/bin/python
import datetime
import time

import cv2 as cv
import numpy as np
from cachetools import TTLCache

from src.common import Heartbeat

from ._analyze import track_fiducial
from ._args import args
from ._comms import Communicator
from ._diagnostics import show_status
from ._display import display_manager
from ._logger import logger

_ALLOWED_DELAY = 5.0  # seconds
_DEFAULT_FPS_RECOMMENDATION = 30.0

_camera_feed_cache = TTLCache(maxsize=100, ttl=10)
_camera_feed_window_manager_heartbeat = Heartbeat(5)
_fiducial_cache = TTLCache(maxsize=10, ttl=5)
_fiducial_publisher_heartbeat = Heartbeat(1 / args.frequency)

logger.info("Starting fiducial tracker server.")

show_status(running=True)

try:
  with Communicator(args.location_stream_address, args.video_stream_address) as comms:
    while req := comms.recv_video_stream():
      if req.timestamp + _ALLOWED_DELAY < time.time():
        logger.debug("Received request is stale and was discarded.")

        comms.send_video_stream(_DEFAULT_FPS_RECOMMENDATION)
        continue  # skip rest of loop

      # log connected camera uuid
      _camera_feed_cache[req.camera_id] = None

      if _fiducial_publisher_heartbeat.has_interval_passed():
        logger.debug("Sending fiducial locations to clients.")

        comms.send_location_stream(fiducials=list(_fiducial_cache.values()))

      processing_start_time = time.time()

      frame = np.frombuffer(req.frame, dtype=np.uint8).reshape(req.shape)

      if args.display_raw_frames:
        display_manager.display(f"Raw stream ({req.camera_id})", frame)

      track_fiducial(frame, req, _fiducial_cache, draw=args.display_processed_frames)

      if args.display_processed_frames:
        display_manager.display(f"Processed stream ({req.camera_id})", frame)

      if _camera_feed_window_manager_heartbeat.has_interval_passed():
        logger.debug("Closing old display windows.")

        display_manager.close_old(_camera_feed_cache.keys())

      recommended_fps = 1 / (time.time() - processing_start_time)
      recommended_fps_balanced = recommended_fps / max(len(_camera_feed_cache), 1)

      comms.send_video_stream(recommended_fps_balanced)
except KeyboardInterrupt:
  pass
finally:
  logger.info("Ending fiducial tracker server.")

  show_status(running=False)

  cv.destroyAllWindows()
