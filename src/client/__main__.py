#!/home/mmirrashed/.conda/envs/tracker/bin/python
from ._args import args
from ._video_reader import VideoReader

from uuid import uuid4

import cv2

CLIENT_ID = uuid4()


with VideoReader(args.source) as vr:
  for frame in vr.frames():
    cv2.imshow("INPUT", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
      break
  cv2.destroyAllWindows()
