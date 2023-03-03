#!/home/mmirrashed/.conda/envs/tracker/bin/python
from src.common.models import Camera

from ._args import args
from ._calibrator import Calibrator
from ._comms import Commmunicator
from ._logger import logger
from ._video_reader import VideoReader

_camera = Camera(args.src)

logger.name = f"{logger.name}:{_camera.id.hex[:4]}"


try:
  if args.camera is not None and args.corners is None:
    logger.debug("Corner coordinates were not provided.")

    with VideoReader(_camera) as video_reader:
      args.corners = Calibrator(video_reader).calibrate()

  with VideoReader(_camera) as video_reader:
    with Commmunicator(args.address, _camera.id, args.corners) as comms:
      logger.info(f"Starting video stream to {args.address}.")

      for frame in video_reader.frames():
        comms.send(frame)

        if res := comms.recv():
          logger.debug(f"Received FPS recommendation of {res.recommended_fps:.1f} FPS.")

          video_reader.fps = res.recommended_fps
        else:
          logger.debug("Timed out on receiving server response.")
except (AssertionError, KeyboardInterrupt):
  logger.info(f"Ending video stream to {args.address}.")
