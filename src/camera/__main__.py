#!/home/mmirrashed/.conda/envs/tracker/bin/python
from uuid import uuid4

from src.common import display

from ._args import args
from ._calibrator import Calibrator
from ._comms import Commmunicator
from ._video_reader import VideoReader

_CAMERA_ID = uuid4()


if args.camera is not None and args.corners is None:
  with VideoReader(args.src) as video_reader:
    args.corners = Calibrator(video_reader).calibrate()

try:
  with VideoReader(args.src) as video_reader:
    with Commmunicator(args.port, _CAMERA_ID, args.corners) as comms:
      display(f"Camera ({_CAMERA_ID}) is streaming video...")

      for frame in video_reader.frames():
        comms.send(frame)

        if res := comms.recv():
          video_reader.fps = res.recommended_fps
except KeyboardInterrupt:
  display(f"Camera ({_CAMERA_ID}) is exiting...")
