#!/home/mmirrashed/.conda/envs/tracker/bin/python
import time

import cv2 as cv
import numpy as np
from cachetools import TTLCache

from src.common import Heartbeat

from ._analyze import track_fiducial
from ._args import args
from ._comms import Communicator
from ._diagnostics import show_status
from ._logger import logger

_camera_feed_cache = TTLCache(maxsize=100, ttl=10)
_fiducial_cache = TTLCache(maxsize=10, ttl=5)
_fiducial_publisher_heartbeat = Heartbeat(1 / args.frequency)

logger.info(f"Starting fiducial tracker server.")

show_status(running=True)

try:
  with Communicator(args.location_stream_address, args.video_stream_address) as comms:
    while req := comms.recv_video_stream():
      # log connected camera uuid
      _camera_feed_cache[req.camera_id] = None

      if _fiducial_publisher_heartbeat.has_interval_passed():
        comms.send_location_stream(fiducials=list(_fiducial_cache.values()))

      processing_start_time = time.time()

      frame = np.frombuffer(req.frame, dtype=np.uint8).reshape(req.shape)

      if args.display_raw_frames:
        cv.imshow(f"Raw stream ({req.camera_id})", frame)
        cv.waitKey(1)

      track_fiducial(frame, req, _fiducial_cache, draw=args.display_processed_frames)

      if args.display_processed_frames:
        cv.imshow(f"Processed stream ({req.camera_id})", frame)
        cv.waitKey(1)

      recommended_fps = 1 / (time.time() - processing_start_time)
      recommended_fps_balanced = recommended_fps / len(camera_cache)

      comms.send_video_stream(recommended_fps_balanced)
except KeyboardInterrupt:
  pass
finally:
  logger.info("Ending fiducial tracker server.")

  show_status(running=False)

  cv.destroyAllWindows()
