#!/home/mmirrashed/.conda/envs/tracker/bin/python
from src.common import display

from ._args import args
from ._comms import Communicator

import cv2 as cv
import qoi

RECOMMENDED_FPS = 30


try:
  with Communicator(args.location_stream_port, args.video_stream_port) as comms:
    while req := comms.recv_video_stream():
      cv.imshow("Camera stream", qoi.decode(req.frame_encoded))

      comms.send_video_stream(RECOMMENDED_FPS)

      if cv.waitKey(1) & 0xFF == ord("q"):
        break
except KeyboardInterrupt:
  display("Server is exiting...")
