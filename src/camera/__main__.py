#!/home/mmirrashed/.conda/envs/tracker/bin/python
from uuid import uuid4

from src.common import display

from ._args import args
from ._calibrator import Calibrator
from ._comms import Commmunicator
from ._video_reader import VideoReader

CAMERA_ID = uuid4()


if args.camera is not None and args.corners is None:
  with VideoReader(args.source) as video_reader:
    args.corners = Calibrator(video_reader).calibrate()

try:
  with VideoReader(args.source) as video_reader:
    with Commmunicator(args.port, CAMERA_ID, args.corners) as comms:
      display(f"Camera ({CAMERA_ID}) is streaming video...")

      for frame in video_reader.frames():
        comms.send(frame)
except KeyboardInterrupt:
  display(f"Camera ({CAMERA_ID}) is exiting...")
