#!/home/mmirrashed/.conda/envs/tracker/bin/python
from uuid import uuid4

from src.common import display

from ._args import args
from ._comms import Commmunicator
from ._video_reader import VideoReader

CLIENT_ID = uuid4()


try:
  with VideoReader(args.source) as video_reader:
    with Commmunicator(args.port, CLIENT_ID) as comms:
      display(f"Client ({CLIENT_ID}) is streaming video...")

      for frame in video_reader.frames():
        comms.send(frame)
except KeyboardInterrupt:
  display(f"Client ({CLIENT_ID}) is exiting...")
