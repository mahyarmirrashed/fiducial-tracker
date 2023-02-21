#!/home/mmirrashed/.conda/envs/tracker/bin/python
from src.common import display
from src.common.models import Camera

from ._args import args
from ._calibrator import Calibrator
from ._comms import Commmunicator
from ._video_reader import VideoReader

_camera = Camera(args.src)


try:
  if args.camera is not None and args.corners is None:
    with VideoReader(_camera) as video_reader:
      args.corners = Calibrator(video_reader).calibrate()

  with VideoReader(args.src) as video_reader:
    with Commmunicator(args.port, _camera.id, args.corners) as comms:
      display(f"{_camera} is streaming video...")

      for frame in video_reader.frames():
        comms.send(frame)

        if res := comms.recv():
          video_reader.fps = res.recommended_fps
except (AssertionError, KeyboardInterrupt):
  display(f"{_camera} is exiting...")
