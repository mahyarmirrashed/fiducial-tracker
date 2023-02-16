#!/home/mmirrashed/.conda/envs/tracker/bin/python
from cachetools import TTLCache
from typing import Union

from src.common import display
from src.common.models import Fiducial, Point, VideoStreamRequestMessage

from ._args import args
from ._comms import Communicator
from ._delta_tracker import time_since_last_call
from .darknet import darknet

import cv2 as cv
import qoi
import uuid

DEFAULT_FIDUCIAL_ID = ""
RECOMMENDED_FPS = 30


camera_cache: TTLCache[uuid.UUID, None] = TTLCache(maxsize=100, ttl=60)
fiducial_cache: TTLCache[str, Fiducial] = TTLCache(maxsize=10, ttl=5)

delta_tracker = time_since_last_call()

network = darknet.load(args.config, args.data, args.weights)
network_image_buffer = darknet.get_image_buffer(network)

req: Union[VideoStreamRequestMessage, None]

try:
  with Communicator(args.location_stream_port, args.video_stream_port) as comms:
    while req := comms.recv_video_stream():
      camera_cache[req.camera_id] = None

      frame = qoi.decode(req.frame_encoded)
      frame_rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
      frame_rsz = cv.resize(
        frame_rgb, (network.width, network.height), interpolation=cv.INTER_LINEAR
      )

      darknet.load_image_buffer(network_image_buffer, frame_rsz.tobytes())
      predictions = darknet.get_predictions(
        network, network_image_buffer, threshold=args.confidence_threshold
      )

      for prediction in predictions:
        prediction.bounding_box = prediction.bounding_box.normalize_to(
          network.width,
          network.height,
        ).scale_to(
          req.get_view_width(),
          req.get_view_height(),
        )

      if len(predictions) > 0:
        bounding_box = predictions[0].bounding_box

        fiducial_cache[DEFAULT_FIDUCIAL_ID] = Fiducial(
          DEFAULT_FIDUCIAL_ID,
          location=Point(x=int(bounding_box.x), y=int(bounding_box.y)),
          heading=None,
        )

      recommended_fps = 1 / next(time_since_last_call())
      recommended_fps_balanced = recommended_fps / len(camera_cache)

      comms.send_video_stream(recommended_fps_balanced)
except KeyboardInterrupt:
  display("Server is exiting...")
finally:
  darknet.free_image_buffer(network_image_buffer)
